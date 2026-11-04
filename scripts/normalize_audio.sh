#!/usr/bin/env bash
set -euo pipefail
cd /workspace/FTI-SIDE
mkdir -p studio/public/audio
if [ -f studio/public/audio/podcast-normalized.m4a ]; then
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 studio/public/audio/podcast-normalized.m4a
  exit 0
fi
ffmpeg -nostdin -hide_banner -nostats -i studio/public/sources/podcast.mp4 -vn -af 'loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=-18.28:measured_TP=0.65:measured_LRA=14.20:measured_thresh=-29.48:offset=2.63:linear=false:print_format=json' -ar 48000 -ac 2 -c:a aac -b:a 256k studio/public/audio/podcast-normalized.m4a 2> docs/audio-normalization.log
