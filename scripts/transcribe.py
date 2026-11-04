"""Local multilingual transcription; outputs are machine drafts until reviewed."""
import argparse
import json
from pathlib import Path
from faster_whisper import WhisperModel, BatchedInferencePipeline

p = argparse.ArgumentParser()
p.add_argument('audio')
p.add_argument('--model', default='small')
p.add_argument('--out', default='docs/transcription')
p.add_argument('--batch-size', type=int, default=8)
a = p.parse_args()
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)
model = WhisperModel(a.model, device='cpu', compute_type='int8', cpu_threads=4)
pipeline = BatchedInferencePipeline(model=model)
segments, info = pipeline.transcribe(a.audio, language='id', word_timestamps=True, vad_filter=True, beam_size=5, batch_size=a.batch_size, condition_on_previous_text=False, repetition_penalty=1.08, no_repeat_ngram_size=3, initial_prompt='Podcast FTI SIDE, BEM FTI Universitas Trisakti, Kabinet ARKA. Pembicara: Nadya, Ghivariel, Kinan, Cahaya. Organisasi, kuliah, manajemen waktu, kepemimpinan.')
rows, captions = [], []
if (out/'segments.draft.jsonl').exists():
    raise SystemExit('Output already exists; use another --out directory to preserve prior work')
for segment in segments:
    row = {'start': segment.start, 'end': segment.end, 'text': segment.text, 'avg_logprob': segment.avg_logprob, 'no_speech_prob': segment.no_speech_prob, 'words': [{'word': w.word, 'start': w.start, 'end': w.end, 'probability': w.probability} for w in segment.words or []]}
    rows.append(row)
    for w in segment.words or []:
        captions.append({'text': w.word, 'startMs': round(w.start*1000), 'endMs': round(w.end*1000), 'timestampMs': round(w.start*1000), 'confidence': w.probability})
    with (out/'segments.draft.jsonl').open('a') as f:
        f.write(json.dumps(row, ensure_ascii=False)+'\n')
    print(f'{segment.start:.2f}-{segment.end:.2f} {segment.text}', flush=True)
(out/'segments.draft.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
(out/'captions.draft.json').write_text(json.dumps(captions, ensure_ascii=False, indent=2))
(out/'transcript.draft.txt').write_text('\n'.join(f"[{r['start']:.2f} - {r['end']:.2f}] {r['text']}" for r in rows))
(out/'metadata.json').write_text(json.dumps({'language': info.language, 'duration': info.duration, 'reviewed': False, 'model': a.model}, indent=2))
