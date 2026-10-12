#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR/marca/motion/logo-circular"
if command -v npx >/dev/null 2>&1; then
  AL_HF=(npx --yes hyperframes@0.8.145)
elif command -v pnpm >/dev/null 2>&1; then
  AL_HF=(pnpm dlx hyperframes@0.8.145)
else
  echo "Instala Node.js y npx o pnpm para renderizar HyperFrames." >&2
  exit 1
fi
"${AL_HF[@]}" check .
"${AL_HF[@]}" render --format png-sequence --output renders/secuencia-png --fps 30 --quality high --workers 2
ffmpeg -hide_banner -loglevel error -framerate 30 -i renders/secuencia-png/frame_%06d.png -plays 0 -f apng -y renders/AL-DESTINO-logo-circular-animado.png

cp renders/secuencia-png/frame_000096.png renders/logo-circular-poster.png
