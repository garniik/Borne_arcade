from ollama_wrapper_iut import OllamaWrapper
import argparse
import json
import math
import os
from pathlib import Path


# -------- Utils --------

def analyser_projet(project_path="../borne_arcade"):
    """Analyse tous les fichiers du projet borne_arcade"""
    documents = []
    project_dir = Path(project_path)
    
    if not project_dir.exists():
        raise FileNotFoundError(f"Le projet {project_path} n'existe pas")
    
    print(f"📂 Analyse du projet : {project_dir}")
    
    # Extensions de fichiers à analyser
    extensions = {'.py', '.java', '.sh', '.md', '.txt', '.json', '.yaml', '.yml', '.xml', '.html', '.css'}
    
    # Dossiers à ignorer
    ignore_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea', 'build', 'dist', 'venv'}
    
    for file_path in project_dir.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            # Vérifier que le fichier n'est pas dans un dossier ignoré
            if not any(part in ignore_dirs for part in file_path.parts):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    relative_path = file_path.relative_to(project_dir)
                    
                    document = {
                        'title': str(relative_path),
                        'content': content,
                        'language': file_path.suffix.lower().replace('.', ''),
                        'size': len(content)
                    }
                    documents.append(document)
                    print(f"  ✓ {relative_path} ({file_path.suffix})")
                    
                except UnicodeDecodeError:
                    print(f"  ✗ {file_path} (binaire)")
                except Exception as e:
                    print(f"  ✗ {file_path}: {e}")
    
    print(f"\n✓ {len(documents)} fichiers analysés\n")
    return documents


def lister_projets(projects_root: str = "../borne_arcade/projet"):
    """Liste les sous-projets (jeux) dans le dossier projet/."""
    root = Path(projects_root)
    if not root.exists():
        raise FileNotFoundError(f"Le dossier des projets n'existe pas: {root}")

    ignore_dirs = {".git", "__pycache__", "node_modules", ".vscode", ".idea", "build", "dist", "venv"}
    projets = []
    for p in sorted(root.iterdir()):
        if p.is_dir() and p.name not in ignore_dirs:
            projets.append(p)
    return projets


def doc_est_suffisante(doc_path: Path, *, min_chars: int, min_sections: int) -> bool:
    """Vérifie rapidement si une doc existante est "suffisante".

    Heuristique simple (rapide et offline) :
    - longueur minimale
    - nombre minimal de sections Markdown "## "
    """
    try:
        if not doc_path.exists():
            return False

        content = doc_path.read_text(encoding="utf-8", errors="replace")
        char_count = len(content.strip())
        section_count = content.count("\n## ")

        if char_count < min_chars:
            return False

        if section_count < min_sections:
            return False

        return True
    except Exception:
        return False


def similarite_cosinus(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm = math.sqrt(sum(a*a for a in v1)) * math.sqrt(sum(b*b for b in v2))
    return dot / norm if norm else 0.0


# -------- RAG --------

def rechercher_documents(wrapper, requete, documents, model_embed, top_k=3):
    """Recherche les documents les plus pertinents pour une requête"""
    try:
        requete_emb = wrapper.embed(model=model_embed, text=requete)
    except Exception as e:
        print(f"⚠️  Embeddings non disponibles: {e}")
        # Fallback : recherche par mots-clés
        return rechercher_documents_mots_cles(requete, documents, top_k)
    
    scores = []
    for doc in documents:
        texte = f"{doc['title']}. {doc['content'][:1000]}"  # Limiter la taille
        try:
            doc_emb = wrapper.embed(model=model_embed, text=texte)
            score = similarite_cosinus(requete_emb, doc_emb)
            scores.append((doc, score))
        except Exception as e:
            print(f"  ⚠️  Erreur embedding pour {doc['title']}: {e}")
            scores.append((doc, 0.0))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]


def rechercher_documents_mots_cles(requete, documents, top_k=3):
    """Recherche par mots-clés si les embeddings ne fonctionnent pas"""
    query_words = set(requete.lower().split())
    scores = []
    
    for doc in documents:
        content_lower = doc['content'].lower()
        title_lower = doc['title'].lower()
        score = 0
        
        # Compter les occurrences des mots de la requête
        for word in query_words:
            if word in content_lower:
                score += content_lower.count(word)
            if word in title_lower:
                score += title_lower.count(word) * 2  # Bonus pour le titre
        
        if score > 0:
            scores.append((doc, float(score)))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]


def creer_prompt(requete, documents):
    """Crée un prompt pour générer de la documentation avec une sélection optimisée de fichiers"""
    # Stratégie : sélectionner les fichiers les plus pertinents selon la question
    max_fichiers = 8  # Réduit pour éviter les timeouts
    max_caracteres_par_fichier = 800  # Réduit la taille par fichier
    
    # Sélection intelligente des fichiers selon le type de question
    if "architecture" in requete.lower():
        # Prioriser les fichiers de structure et configuration
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['main', 'config', 'readme', 'update', 'menu'])]
    elif "installer" in requete.lower() or "configurer" in requete.lower():
        # Prioriser les fichiers d'installation et documentation
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['readme', 'install', 'setup', 'config', 'sh'])]
    elif "jeux" in requete.lower():
        # Prioriser les fichiers de jeux
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['game', 'jeu', 'tron', 'pong', 'piano', 'snake'])]
    else:
        # Sélection par défaut : fichiers principaux
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['main', 'game', 'menu', 'readme'])]
    
    # Compléter avec d'autres fichiers si nécessaire
    autres_fichiers = [doc for doc in documents if doc not in fichiers_prioritaires]
    documents_contexte = (fichiers_prioritaires + autres_fichiers)[:max_fichiers]
    
    contexte = "\n\n".join(
        f"[Fichier {i}] {doc['title']}\n```{doc.get('language', 'text')}\n{doc['content'][:max_caracteres_par_fichier]}```"
        for i, doc in enumerate(documents_contexte, 1)
    )

    return f"""
Tu es un assistant technique qui génère de la documentation pour un projet de borne d'arcade.
Base-toi sur les fichiers de code fournis pour répondre.

Fichiers du projet ({len(documents_contexte)} fichiers sélectionnés) :
{contexte}

Question : {requete}

CONSIGNES :
- Réponds en te basant sur les fichiers fournis
- Sois précis et technique , et reste concis
- Génère une documentation claire et structurée

Réponse :
"""


def repondre(wrapper, requete, documents, model_llm, model_embed):
    """Génère une réponse/documentation pour une requête en utilisant une sélection optimisée de fichiers"""
    print(f"\n📝 Question : {requete}")
    print(f"📁 Analyse de {len(documents)} fichiers du projet...")
    
    # Afficher les fichiers qui seront utilisés
    max_fichiers = 8
    if "architecture" in requete.lower():
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['main', 'config', 'readme', 'update', 'menu'])]
    elif "installer" in requete.lower() or "configurer" in requete.lower():
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['readme', 'install', 'setup', 'config', 'sh'])]
    elif "jeux" in requete.lower():
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['game', 'jeu', 'tron', 'pong', 'piano', 'snake'])]
    else:
        fichiers_prioritaires = [doc for doc in documents 
                               if any(x in doc['title'].lower() for x in ['main', 'game', 'menu', 'readme'])]
    
    autres_fichiers = [doc for doc in documents if doc not in fichiers_prioritaires]
    documents_selectionnes = (fichiers_prioritaires + autres_fichiers)[:max_fichiers]
    
    print(f"📋 Fichiers sélectionnés ({len(documents_selectionnes)}):")
    for i, doc in enumerate(documents_selectionnes, 1):
        print(f"  [{i}] {doc['title']}")

    prompt = creer_prompt(requete, documents)
    response = wrapper.generate_text(model=model_llm, prompt=prompt)

    print("\n📄 Documentation générée :")
    print("=" * 70)
    print(response.response)
    print("=" * 70)


def generer_reponse(wrapper, requete, documents, model_llm):
    """Génère une réponse (texte) sans affichage détaillé."""
    prompt = creer_prompt(requete, documents)
    response = wrapper.generate_text(model=model_llm, prompt=prompt)
    return response.response


def _selectionner_fichiers_pour_verif(documents, max_fichiers: int = 8, max_caracteres_par_fichier: int = 900):
    """Sélectionne quelques fichiers représentatifs pour la vérification IA."""
    documents_tries = sorted(documents, key=lambda d: (-d.get("size", 0), d.get("title", "")))
    selection = []
    for doc in documents_tries:
        if len(selection) >= max_fichiers:
            break
        selection.append(
            {
                "title": doc.get("title", ""),
                "language": doc.get("language", "text"),
                "content": (doc.get("content", "")[:max_caracteres_par_fichier]),
            }
        )
    return selection


def doc_est_a_jour_ia(wrapper, *, model_llm: str, doc_path: Path, project_dir: Path) -> bool:
    """Demande à l'IA de valider si la doc existante correspond toujours au code.

    Retourne True uniquement si la première ligne commence par "OK:".
    """
    if not doc_path.exists():
        return False

    doc_content = doc_path.read_text(encoding="utf-8", errors="replace")

    # Re-scan des fichiers du projet
    documents = analyser_projet(str(project_dir))
    fichiers = _selectionner_fichiers_pour_verif(documents)

    contexte = "\n\n".join(
        f"[Fichier {i}] {d['title']}\n```{d['language']}\n{d['content']}\n```"
        for i, d in enumerate(fichiers, 1)
    )

    prompt = f"""
Tu es un relecteur technique. Tu dois vérifier si une documentation Markdown décrit correctement un projet de jeu (borne arcade).

On te donne :
1) la documentation existante
2) des extraits de fichiers du projet

TÂCHE
- Dis si la doc est À JOUR par rapport au code.
- Réponds STRICTEMENT avec UNE ligne au début :
  - OK: <raison courte>
  - ou KO: <raison courte>

RÈGLES
- Si tu n'es pas sûr => KO
- Si la doc décrit des éléments absents du code fourni => KO
- Si la doc oublie des éléments évidents visibles dans les extraits (lancement, contrôles, classes principales) => KO

DOCUMENTATION EXISTANTE:
```markdown
{doc_content[:2500]}
```

FICHIERS PROJET (extraits):
{contexte}
"""

    try:
        response = wrapper.generate_text(model=model_llm, prompt=prompt)
        text = (response.response or "").strip()
    except Exception:
        return False

    first_line = text.splitlines()[0].strip() if text else ""
    return first_line.startswith("OK:")


# -------- Main --------

def main():
    try:
        script_dir = Path(__file__).resolve().parent
        repo_root = script_dir.parent

        parser = argparse.ArgumentParser(description="Générateur de documentation (projet par projet)")
        parser.add_argument(
            "--projects-root",
            default=str(repo_root / "borne_arcade" / "projet"),
            help="Dossier contenant les jeux (projet/)"
        )
        parser.add_argument(
            "--output-dir",
            default=str(script_dir / "generated_docs"),
            help="Dossier de sortie pour les docs générées"
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Régénère la doc même si un fichier existe déjà et semble suffisant"
        )
        parser.add_argument(
            "--min-chars",
            type=int,
            default=1500,
            help="Seuil minimal de caractères pour considérer une doc comme suffisante"
        )
        parser.add_argument(
            "--min-sections",
            type=int,
            default=3,
            help="Nombre minimal de sections '##' pour considérer une doc comme suffisante"
        )
        parser.add_argument(
            "--check-mode",
            choices=["ai", "heuristic"],
            default="ai",
            help="Mode pour décider si une doc existante doit être régénérée (ai=Ollama OK/KO, heuristic=taille/sections)"
        )
        args = parser.parse_args()

        projects_root = Path(args.projects_root)
        if not projects_root.is_absolute():
            projects_root = (script_dir / projects_root).resolve()

        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = (script_dir / output_dir).resolve()

        wrapper = OllamaWrapper()

        models = wrapper.list_models()
        print("Modèles disponibles:", [m.name for m in models])
        
        model_embed = models[0].name if models else "gemma2:latest"
        model_llm = models[1].name if len(models) > 1 else "gemma2:latest"

        print(f"\n🔧 Configuration:")
        print(f"  - Modèle embeddings: {model_embed}")
        print(f"  - Modèle LLM: {model_llm}")

        output_dir.mkdir(parents=True, exist_ok=True)

        projets = lister_projets(str(projects_root))
        print(f"\n📦 {len(projets)} projets trouvés dans: {projects_root}")

        for projet_dir in projets:
            nom_projet = projet_dir.name
            print(f"\n{'=' * 70}")
            print(f"🎮 Projet: {nom_projet}")
            print(f"{'=' * 70}")

            fichier_sortie = output_dir / f"{nom_projet}.md"
            if not args.force and fichier_sortie.exists():
                print(f"⏭️  Doc déjà existante, génération ignorée: {fichier_sortie}")
                continue

            # Analyse: on prend tous les fichiers du projet courant
            documents = analyser_projet(str(projet_dir))
            print(f"  - Documents: {len(documents)} fichiers")

            # Questions centrées sur le jeu
            questions_documentation = [
                f"Décris le jeu {nom_projet} (objectif, principe, gameplay) en te basant sur le code.",
                f"Quels sont les contrôles du jeu {nom_projet} sur la borne arcade (touches/boutons) ?",
                f"Comment lancer et quitter le jeu {nom_projet} (scripts, classe main, commande) ?",
                f"Quelles sont les classes principales et leurs responsabilités dans {nom_projet} ?",
            ]

            contenu_md = f"# {nom_projet}\n\n"
            for question in questions_documentation:
                contenu_md += f"## {question}\n\n"
                contenu_md += generer_reponse(wrapper, question, documents, model_llm)
                contenu_md += "\n\n"

            fichier_sortie.write_text(contenu_md, encoding="utf-8")
            print(f"✅ Documentation générée: {fichier_sortie}")

    except Exception as e:
        print(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
