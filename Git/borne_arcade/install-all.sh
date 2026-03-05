#!/usr/bin/env bash
set -euo pipefail

# Script unique d'installation de la borne arcade.
# - Dépendances APT (Java, Python, libs SDL pour pygame, outils)
# - Installation MG2D (copie dans le HOME + CLASSPATH, selon doc MG2D)
# - Dépendances Python (venv + pip install -r requirements.txt)
#
# Usage:
#   sudo ./install-all.sh
#
# Options:
#   --venv <path>        Chemin du venv (défaut: <repo>/.venv)
#   --no-java            N'installe pas Java
#   --no-mg2d            N'installe pas MG2D
#   --mg2d-url <url>     URL d'archive MG2D_xxx.zip (si MG2D n'est pas présent localement)
#   --mg2d-zip <path>    Archive MG2D_*.zip locale
#


SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_DIR="$SCRIPT_DIR"

VENV_DIR="$REPO_DIR/.venv"
INSTALL_JAVA=1
INSTALL_MG2D=1
MG2D_URL="https://github.com/synave/MG2D.git"
MG2D_ZIP=""

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
    --no-mg2d)
      INSTALL_MG2D=0
      shift 1
      ;;
    --mg2d-url)
      MG2D_URL="$2"
      shift 2
      ;;
    --mg2d-zip)
      MG2D_ZIP="$2"
      shift 2
      ;;
    -h|--help)
      sed -n '1,120p' "$0"
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
  echo "Ex: sudo ./install-all.sh" >&2
  exit 1
fi

TARGET_USER="${SUDO_USER:-}"
if [[ -z "$TARGET_USER" || "$TARGET_USER" == "root" ]]; then
  echo "⚠️  SUDO_USER introuvable. MG2D/venv seront installés pour root." >&2
  TARGET_USER="root"
fi

TARGET_HOME="$(getent passwd "$TARGET_USER" | cut -d: -f6)"
if [[ -z "$TARGET_HOME" ]]; then
  echo "Impossible de déterminer le HOME de l'utilisateur: $TARGET_USER" >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive

echo "[1/5] APT update"
apt-get update

echo "[2/5] Installation dépendances système"
APT_PACKAGES=(
  git
  ca-certificates
  curl
  unzip
  wget
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
  APT_PACKAGES+=(default-jdk)
fi

apt-get install -y "${APT_PACKAGES[@]}"

echo "[3/5] Installation MG2D (si demandé)"
if [[ "$INSTALL_MG2D" -eq 1 ]]; then
  if [[ -d "$TARGET_HOME/MG2D" ]]; then
    echo "✓ MG2D déjà présent dans: $TARGET_HOME/MG2D"
  else
    TMP_DIR="$(mktemp -d)"
    cleanup() { rm -rf "$TMP_DIR"; }
    trap cleanup EXIT

    ZIP_PATH=""
    if [[ -n "$MG2D_ZIP" ]]; then
      if [[ ! -f "$MG2D_ZIP" ]]; then
        echo "Archive MG2D introuvable: $MG2D_ZIP" >&2
        exit 1
      fi
      ZIP_PATH="$MG2D_ZIP"
    else
      echo "Téléchargement MG2D depuis: $MG2D_URL"
      ZIP_PATH="$TMP_DIR/MG2D.zip"
      wget -O "$ZIP_PATH" "$MG2D_URL"
    fi

    echo "Décompression…"
    unzip -q "$ZIP_PATH" -d "$TMP_DIR/mg2d_extract"

    # La doc MG2D indique que l'archive contient un dossier MG2D_xxx/ avec un sous-dossier MG2D/
    MG2D_DIR_FOUND="$(find "$TMP_DIR/mg2d_extract" -maxdepth 3 -type d -name MG2D | head -n 1 || true)"
    if [[ -z "$MG2D_DIR_FOUND" ]]; then
      echo "Impossible de trouver le dossier MG2D dans l'archive." >&2
      exit 1
    fi

    echo "Copie de MG2D vers $TARGET_HOME/MG2D"
    rm -rf "$TARGET_HOME/MG2D" || true
    cp -R "$MG2D_DIR_FOUND" "$TARGET_HOME/MG2D"
    chown -R "$TARGET_USER":"$TARGET_USER" "$TARGET_HOME/MG2D"
  fi

  BASHRC="$TARGET_HOME/.bashrc"
  touch "$BASHRC"
  chown "$TARGET_USER":"$TARGET_USER" "$BASHRC"

  # Suivre la doc MG2D: export CLASSPATH=$CLASSPATH:.:~
  if ! grep -q "export CLASSPATH=\$CLASSPATH:.:~" "$BASHRC"; then
    echo "Ajout CLASSPATH dans $BASHRC"
    echo "export CLASSPATH=\$CLASSPATH:.:~" >> "$BASHRC"
  else
    echo "✓ CLASSPATH déjà configuré dans $BASHRC"
  fi
else
  echo "(MG2D ignoré --no-mg2d)"
fi

echo "[4/5] Installation dépendances Python (venv + requirements)"
# On installe le venv côté repo, mais on le met propriétaire de l'utilisateur (utile pour lancer sans root)
python3 -m venv "$VENV_DIR"
chown -R "$TARGET_USER":"$TARGET_USER" "$VENV_DIR"

# Installer en tant que TARGET_USER (évite des fichiers root dans le venv)
run_as_user() {
  if [[ "$TARGET_USER" == "root" ]]; then
    bash -lc "$*"
  else
    su - "$TARGET_USER" -c "$*"
  fi
}

run_as_user "source '$VENV_DIR/bin/activate' && python -m pip install --upgrade pip setuptools wheel"

REQ_FILES=()
while IFS= read -r -d '' f; do
  REQ_FILES+=("$f")
done < <(find "$REPO_DIR/projet" -name requirements.txt -type f -print0 2>/dev/null || true)

if [[ ${#REQ_FILES[@]} -eq 0 ]]; then
  echo "⚠️  Aucun requirements.txt trouvé dans $REPO_DIR/projet" >&2
else
  for rf in "${REQ_FILES[@]}"; do
    echo "  - pip install -r $rf"
    run_as_user "source '$VENV_DIR/bin/activate' && python -m pip install -r '$rf'"
  done
fi

# Sécurité: au moins pygame
if ! run_as_user "source '$VENV_DIR/bin/activate' && python -c 'import pygame'" >/dev/null 2>&1; then
  echo "⚠️  pygame non importable, tentative pip install pygame" >&2
  run_as_user "source '$VENV_DIR/bin/activate' && python -m pip install pygame"
fi

#ajouter cette commande pour attribuer les touche correctement
cp $SCRIPT_DIR/borne   /usr/share/X11/xkb/symbols/borne

# Ajouter le lancement automatique de la borne
mkdir -p $HOME/.config/autostart
cp $REPO_DIR/borne.desktop $HOME/.config/autostart/

echo "[5/5] Résumé"
echo "✅ Installation terminée"
echo "- Utilisateur cible: $TARGET_USER"
echo "- HOME utilisateur: $TARGET_HOME"
echo "- Venv:            $VENV_DIR"
if [[ "$INSTALL_JAVA" -eq 1 ]]; then
  echo "- Java:            installé"
else
  echo "- Java:            ignoré"
fi
if [[ "$INSTALL_MG2D" -eq 1 ]]; then
  echo "- MG2D:            installé (ou déjà présent)"
else
  echo "- MG2D:            ignoré"
fi

echo "\nConseils:"
echo "- Ouvre un nouveau terminal pour que le CLASSPATH prenne effet (MG2D)."
echo "- Active le venv pour lancer les jeux Python: source '$VENV_DIR/bin/activate'"
