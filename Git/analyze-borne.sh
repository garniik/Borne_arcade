#!/bin/bash
# Script d'analyse complet de la borne arcade

echo "🎮 Analyse complète de la borne arcade et génération de documentation"
echo "=================================================================="

# 1. Analyse de couverture du code
echo "1️⃣ Analyse de couverture du code Java..."
python documentation/scripts/ia-doc-coverage.py borne_arcade/ --output borne-coverage.json

# 2. Analyse de la documentation existante
echo "2️⃣ Analyse de la documentation existante..."
python documentation/scripts/ia-doc-coverage.py documentation/src/ --output doc-coverage.json

# 3. Génération de patches IA
echo "3️⃣ Génération des suggestions de documentation..."
python documentation/scripts/ia-doc-patch.py --dry-run --output borne-patches.json

# 4. Test des liens
echo "4️⃣ Validation des liens..."
python documentation/tests/test_links.py documentation/src/

# 5. Tests de qualité
echo "5️⃣ Tests de qualité de la documentation..."
python documentation/tests/test_coverage.py documentation/src/ --threshold 0.8

# 6. Notes de version
echo "6️⃣ Génération des notes de version..."
python documentation/scripts/ia-release-notes.py --version "v1.0.0" --stdout > release-notes.md

echo ""
echo "✅ Analyse terminée !"
echo ""
echo "📄 Fichiers générés :"
echo "  - borne-coverage.json (couverture du code)"
echo "  - doc-coverage.json (couverture de la doc)"
echo "  - borne-patches.json (suggestions IA)"
echo "  - link-validation-report.md (liens cassés)"
echo "  - coverage-test-results.json (tests qualité)"
echo "  - release-notes.md (notes de version)"
echo ""
echo "📊 Prochaines étapes :"
echo "1. Consulter les rapports générés"
echo "2. Appliquer les suggestions de documentation"
echo "3. Corriger les liens cassés identifiés"
echo "4. Créer les fichiers de documentation manquants"
