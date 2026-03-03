import argparse
import sys
from pathlib import Path

from ollama_wrapper_iut import OllamaWrapper

import Docs_Generator as docs


def _repo_root_from_script() -> Path:
    return Path(__file__).resolve().parent.parent


def generate_markdown_doc(*, wrapper: OllamaWrapper, model_llm: str, documents: list[dict], title: str, questions: list[str]) -> str:
    contenu_md = f"# {title}\n\n"
    for q in questions:
        contenu_md += f"## {q}\n\n"
        contenu_md += docs.generer_reponse(wrapper, q, documents, model_llm)
        contenu_md += "\n\n"
    return contenu_md


def main(argv: list[str] | None = None) -> int:
    script_dir = Path(__file__).resolve().parent
    repo_root = _repo_root_from_script()

    parser = argparse.ArgumentParser(description="Génère automatiquement la documentation (utilisateur/technique) + injection docstrings/Javadoc")
    parser.add_argument(
        "--project-root",
        default=str(repo_root),
        help="Racine du repo à analyser (par défaut: racine du dépôt)",
    )
    parser.add_argument(
        "--output-dir",
        default=str(script_dir / "generated_docs"),
        help="Dossier de sortie des docs Markdown",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Applique les modifications (injection docstrings/Javadoc). Sans ça: dry-run.",
    )
    parser.add_argument(
        "--model-llm",
        default="",
        help="Nom du modèle LLM Ollama (sinon auto: 2e modèle si dispo)",
    )
    parser.add_argument(
        "--model-embed",
        default="",
        help="Nom du modèle embeddings Ollama (sinon auto: 1er modèle si dispo)",
    )
    args = parser.parse_args(argv)

    project_root = Path(args.project_root).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    wrapper = OllamaWrapper()
    models = wrapper.list_models()

    model_embed = args.model_embed or (models[0].name if models else "qwen3:8b")
    model_llm = args.model_llm or (models[1].name if len(models) > 1 else (models[0].name if models else "qwen3:8b"))

    print("🔧 Configuration:")
    print(f"  - project_root: {project_root}")
    print(f"  - output_dir:   {output_dir}")
    print(f"  - model_embed:  {model_embed}")
    print(f"  - model_llm:    {model_llm}")
    print(f"  - mode:         {'APPLY' if args.apply else 'DRY-RUN'}")

    print("\n📂 Analyse du projet…")
    documents = docs.analyser_projet(str(project_root))

    user_questions = [
        "Présente le projet comme un guide utilisateur: à quoi sert la borne, comment lancer, comment quitter.",
        "Décris les contrôles généraux (clavier/boutons) et comment naviguer dans les menus.",
        "Liste les jeux disponibles et explique comment en sélectionner un.",
        "Donne un guide de dépannage utilisateur (erreurs courantes, ressources manquantes, plein écran, sons).",
    ]

    tech_questions = [
        "Décris l'architecture technique globale du dépôt (dossiers principaux, responsabilités).",
        "Explique comment les jeux sont lancés (scripts .sh/.desktop, points d'entrée Python/Java).",
        "Décris la gestion des ressources (images, fonts, sons) et les conventions de chemins.",
        "Explique comment ajouter un nouveau jeu (structure attendue, intégration au menu).",
    ]

    api_questions = [
        "Fais un index API: liste les modules/fichiers importants et leur rôle.",
        "Pour les composants principaux, liste les classes/fonctions publiques importantes et leurs responsabilités.",
    ]

    print("\n📝 Génération docs Markdown…")
    (output_dir / "DOCUMENTATION_UTILISATEUR.md").write_text(
        generate_markdown_doc(wrapper=wrapper, model_llm=model_llm, documents=documents, title="Documentation utilisateur", questions=user_questions),
        encoding="utf-8",
    )
    (output_dir / "DOCUMENTATION_TECHNIQUE.md").write_text(
        generate_markdown_doc(wrapper=wrapper, model_llm=model_llm, documents=documents, title="Documentation technique", questions=tech_questions),
        encoding="utf-8",
    )
    (output_dir / "DOCUMENTATION_API.md").write_text(
        generate_markdown_doc(wrapper=wrapper, model_llm=model_llm, documents=documents, title="Documentation API", questions=api_questions),
        encoding="utf-8",
    )

    print("✅ Docs générées.")

    print("\n🧩 Injection docstrings Python…")
    from inject_docstrings import run as inject_py

    inject_py(
        wrapper=wrapper,
        model_llm=model_llm,
        repo_root=project_root,
        apply=args.apply,
    )

    print("\n🧩 Injection Javadoc Java…")
    from inject_javadoc import run as inject_java

    inject_java(
        wrapper=wrapper,
        model_llm=model_llm,
        repo_root=project_root,
        apply=args.apply,
    )

    print("\n🎉 Terminé.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
