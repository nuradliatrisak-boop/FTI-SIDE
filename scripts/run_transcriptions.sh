#!/usr/bin/env bash
set -euo pipefail
cd /workspace/FTI-SIDE
HF_HUB_DISABLE_XET=1 .venv/bin/python -u scripts/download_model.py
.venv/bin/python -u scripts/transcribe.py docs/opening-mono16k.wav --model models/faster-whisper-small --out docs/opening-transcription
.venv/bin/python -u scripts/transcribe.py docs/podcast-mono16k.wav --model models/faster-whisper-small --out docs/transcription
