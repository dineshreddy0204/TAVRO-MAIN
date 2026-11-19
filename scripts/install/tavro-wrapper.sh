#!/usr/bin/env bash
# tavro-wrapper.sh — symlinked to ~/.local/bin/tavro.
# Activates the managed venv and execs the real tavro CLI.

TAVRO_HOME="${TAVRO_HOME:-$HOME/.tavro}"
VENV="$TAVRO_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "tavro: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/tavro" "$@"
