"""Verify a downloaded original without modifying it; reject HTML/error bodies."""
import argparse
import hashlib
import json
import pathlib
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
parser.add_argument('--report', required=True, type=pathlib.Path)
args = parser.parse_args()
if not args.file.is_file() or args.file.stat().st_size < 1024:
    parser.error('Source absent or too small to be usable video')
probe = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(args.file)], capture_output=True, text=True, check=True)
data = json.loads(probe.stdout)
video = [s for s in data['streams'] if s['codec_type'] == 'video']
audio = [s for s in data['streams'] if s['codec_type'] == 'audio']
if not video or not audio:
    parser.error('Both original video and audio streams are required')
if (video[0]['width'], video[0]['height']) != (1920, 1080):
    parser.error('Source differs from requested Full HD; investigate original before editing')
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-xerror', '-i', str(args.file), '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'], check=True)
sha = hashlib.sha256()
with args.file.open('rb') as source:
    for chunk in iter(lambda: source.read(1024 * 1024), b''):
        sha.update(chunk)
data.update({'source': str(args.file.resolve()), 'size_bytes': args.file.stat().st_size, 'sha256': sha.hexdigest(), 'full_av_decode': 'passed'})
args.report.parent.mkdir(parents=True, exist_ok=True)
args.report.write_text(json.dumps(data, indent=2) + '\n')
print('Verified:', args.file.name, 'duration:', data['format']['duration'])
