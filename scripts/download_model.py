"""Resume official model download via the configured HTTPS proxy; preserve TLS."""
import os
os.environ['HF_HUB_DISABLE_XET'] = '1'
from pathlib import Path
from huggingface_hub import snapshot_download
from faster_whisper import WhisperModel
root = Path(__file__).resolve().parents[1]
path = snapshot_download('Systran/faster-whisper-small', local_dir=str(root/'models/faster-whisper-small'), allow_patterns=['config.json', 'model.bin', 'tokenizer.json', 'vocabulary.txt'])
model = WhisperModel(path, device='cpu', compute_type='int8', cpu_threads=4, local_files_only=True)
print('Model downloaded and loaded:', path)
