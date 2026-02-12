#!/usr/bin/env python3
"""
Exemple d'utilisation complète du OllamaWrapper

Cet exemple montre comment utiliser le wrapper pour différentes tâches :
- Génération de texte
- Génération avec image
- Embeddings
- Gestion des erreurs
"""

import sys
from pathlib import Path

# Ajouter le chemin vers le wrapper
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from ollama_wrapper_iut import OllamaWrapper, OllamaError, OllamaConnectionError


def main():
    """Fonction principale d'exemple."""
    print("🤖 Exemple d'utilisation du OllamaWrapper")
    print("=" * 50)
    
    # Initialisation du client
    client = OllamaWrapper(
        base_url="http://localhost:11434",
        timeout_s=30.0
    )
    
    try:
        # 1. Vérifier que le serveur fonctionne
        print("\n1️⃣ Vérification du serveur...")
        if not client.is_server_running():
            print("❌ Le serveur Ollama n'est pas démarré")
            print("💡 Démarrez-le avec: ollama serve")
            return
        
        print("✅ Serveur Ollama en ligne")
        
        # 2. Obtenir la version
        print("\n2️⃣ Version du serveur:")
        try:
            version = client.get_version()
            print(f"   Version: {version}")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
        
        # 3. Lister les modèles disponibles
        print("\n3️⃣ Modèles disponibles:")
        try:
            models = client.list_models()
            if models:
                for model in models[:5]:  # Limiter à 5 modèles
                    size_mb = (model.size or 0) / (1024 * 1024) if model.size else 0
                    print(f"   • {model.name} ({size_mb:.1f} MB)")
                
                if len(models) > 5:
                    print(f"   ... et {len(models) - 5} autres")
            else:
                print("   Aucun modèle installé")
                print("   💡 Installez un modèle avec: ollama pull gemma2:latest")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
        
        # 4. Génération de texte simple
        print("\n4️⃣ Génération de texte:")
        try:
            result = client.generate_text(
                model="gemma2:latest",  # À adapter selon vos modèles
                prompt="Qu'est-ce que l'intelligence artificielle en une phrase ?",
                options={"temperature": 0.7, "max_tokens": 100}
            )
            
            print(f"   Modèle: {result.model}")
            print(f"   Réponse: {result.response}")
            if result.done:
                print(f"   ⏱️  Durée: {result.total_duration or 0} ns")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
        
        # 5. Génération avec système
        print("\n5️⃣ Génération avec message système:")
        try:
            result = client.generate_text(
                model="gemma2:latest",
                prompt="Explique la photosynthèse simplement",
                system="Tu es un professeur de biologie qui s'adresse à des enfants de 10 ans.",
                options={"temperature": 0.5}
            )
            
            print(f"   Réponse: {result.response}")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
        
        # 6. Embeddings (si le modèle le supporte)
        print("\n6️⃣ Génération d'embeddings:")
        try:
            embedding = client.embed(
                model="nomic-embed-text:latest",  # Modèle d'embedding
                text="Intelligence artificielle et machine learning"
            )
            
            print(f"   Dimension: {len(embedding)}")
            print(f"   Premiers valeurs: {embedding[:5]}...")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
            print("   💡 Vérifiez que le modèle d'embedding est installé")
        
        # 7. Génération avec image (exemple commenté)
        print("\n7️⃣ Génération avec image (exemple):")
        print("   # Code exemple (décommentez pour tester):")
        print("   # result = client.generate_with_image(")
        print("   #     model='llava:latest',")
        print("   #     prompt='Décris cette image',")
        print("   #     image='chemin/vers/image.jpg'")
        print("   # )")
        print("   # print(f'Réponse: {result.response}')")
        
        # Exemple de code commenté
        """
        try:
            result = client.generate_with_image(
                model="llava:latest",
                prompt="Décris cette image en détail",
                image="example.jpg",  # Remplacez par une vraie image
                system="Tu es un expert en analyse d'images"
            )
            print(f"   Réponse: {result.response}")
        except OllamaError as e:
            print(f"   ❌ Erreur: {e}")
        except FileNotFoundError:
            print("   ❌ Fichier image non trouvé")
        """
        
        print("\n✅ Exemple terminé avec succès!")
        
    except OllamaConnectionError as e:
        print(f"❌ Erreur de connexion: {e}")
        print("💡 Vérifiez que Ollama est bien démarré et accessible")
    except OllamaError as e:
        print(f"❌ Erreur Ollama: {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")


def demo_advanced_usage():
    """Démonstration d'utilisation avancée."""
    print("\n🔧 Utilisation avancée:")
    print("-" * 30)
    
    client = OllamaWrapper()
    
    # Options avancées
    advanced_options = {
        "temperature": 0.8,      # Plus de créativité
        "top_p": 0.9,           # Nucleus sampling
        "top_k": 40,            # Top-k sampling
        "seed": 42,             # Reproductibilité
        "num_predict": 200,     # Limiter la longueur
        "repeat_penalty": 1.1   # Éviter les répétitions
    }
    
    try:
        result = client.generate_text(
            model="gemma2:latest",
            prompt="Écris une courte histoire de science-fiction",
            options=advanced_options
        )
        
        print(f"Histoire générée:\n{result.response}")
        
    except OllamaError as e:
        print(f"Erreur: {e}")


def demo_error_handling():
    """Démonstration de la gestion des erreurs."""
    print("\n🛡️ Gestion des erreurs:")
    print("-" * 30)
    
    client = OllamaWrapper()
    
    # Tester différentes erreurs
    test_cases = [
        ("Modèle inexistant", lambda: client.generate_text(
            model="modele_inexistant", 
            prompt="test"
        )),
        ("Timeout", lambda: client.generate_text(
            model="gemma2:latest",
            prompt="test",
            options={"num_predict": 10000}
        )),
    ]
    
    for test_name, test_func in test_cases:
        print(f"\nTest: {test_name}")
        try:
            test_func()
            print("✅ Succès inattendu")
        except OllamaError as e:
            print(f"❌ Erreur attendue: {type(e).__name__}: {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue: {type(e).__name__}: {e}")


if __name__ == "__main__":
    # Exemple principal
    main()
    
    # Exemples additionnels (commentés pour éviter les erreurs)
    # demo_advanced_usage()
    # demo_error_handling()
    
    print("\n" + "=" * 50)
    print("📚 Pour plus d'exemples, voir la documentation complète")
    print("🔗 Lien vers la doc: documentation/src/api/ollama-wrapper.md")
