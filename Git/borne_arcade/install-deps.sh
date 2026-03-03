#!/usr/bin/env bash
set -euo pipefail

# Installation "tout-en-un" des dépendances pour la borne arcade.
# - Dépendances système via APT (Java, Python, libs SDL pour pygame, outils)
# - Dépendances Python via venv + pip (requirements.txt trouvés dans projet/)
#
# Usage:
#   ./install-deps.sh
#   ./install-deps.sh --venv .venv
#   ./install-deps.sh --no-java
#

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_DIR="$SCRIPT_DIR"

VENV_DIR="$REPO_DIR/.venv"
INSTALL_JAVA=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --venv)
      VENV_DIR="$2"
      shift 2
      ;;
    --no-java)
      INSTALL_JAVA=0
      shift 1
      ;;
    -h|--help)
      sed -n '1,80p' "$0"
      exit 0
      ;;
    *)
      echo "Argument inconnu: $1" >&2
      exit 2
      ;;
  esac
done

if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
  echo "Ce script doit être lancé en root (sudo)." >&2
  echo "Ex: sudo ./install-deps.sh" >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive

echo "[1/4] APT update"
apt-get update

echo "[2/4] Installation dépendances système"
APT_PACKAGES=(
  git
  ca-certificates
  curl
  unzip
  build-essential
  python3
  python3-pip
  python3-venv
  python3-dev
  # Libs SDL courantes requises par pygame (selon distro)
  libsdl2-2.0-0
  libsdl2-image-2.0-0
  libsdl2-mixer-2.0-0
  libsdl2-ttf-2.0-0
  libfreetype6
  libjpeg62-turbo
  libpng16-16
)

if [[ "$INSTALL_JAVA" -eq 1 ]]; then
  # "default-jdk" est plus portable que openjdk-8-jdk (selon versions Debian/Raspbian)
  APT_PACKAGES+=(default-jdk)
fi

apt-get install -y "${APT_PACKAGES[@]}"

echo "[3/4] Installation dépendances Python dans un venv"
python3 -m venv "$VENV_DIR"
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip setuptools wheel

# Installe tous les requirements.txt trouvés dans projet/
REQ_FILES=()
while IFS= read -r -d '' f; do
  REQ_FILES+=("$f")
done < <(find "$REPO_DIR/projet" -name requirements.txt -type f -print0 2>/dev/null || true)

if [[ ${#REQ_FILES[@]} -eq 0 ]]; then
  echo "⚠️  Aucun requirements.txt trouvé dans $REPO_DIR/projet" >&2
  echo "    -> je n'installe pas de dépendances pip spécifiques." >&2
else
  for rf in "${REQ_FILES[@]}"; do
    echo "  - pip install -r $rf"
    python -m pip install -r "$rf"
  done
fi

# Fallback: au moins pygame si aucun requirements (sécurité)
if ! python -c "import pygame" >/dev/null 2>&1; then
  echo "⚠️  pygame non importable après installation, tentative d'installation pip 'pygame'" >&2
  python -m pip install pygame
fi

deactivate || true

echo "[4/4] Résumé"
echo "✅ OK"
echo "- Venv: $VENV_DIR"
if [[ "$INSTALL_JAVA" -eq 1 ]]; then
  echo "- Java: installé"
else
  echo "- Java: ignoré (--no-java)"
fi

echo "\nConseil: pour lancer avec le venv, tu peux faire:"
echo "  source $VENV_DIR/bin/activate"
