# FTI SIDE — Remotion

Baca ../docs/brief.txt, ../docs/STATUS.md, dan ../docs/SOURCES.md.

Node 24, Remotion 4.0.540.

```sh
npm ci --proxy="$HTTPS_PROXY" --https-proxy="$HTTPS_PROXY"
npm run dev
npm run lint
```

Komposisi FTI-SIDE-Opening-Design adalah studi tipografi 10 detik tanpa audio, bukan opening final.

```sh
npx remotion render FTI-SIDE-Opening-Design ../deliverables/OPENING-DESIGN-PREVIEW.mp4 --browser-executable=/usr/bin/chromium --codec=h264 --concurrency=2
```

Footage asli tersimpan di public/sources dan dikecualikan dari Git. Jangan mengunduh ulang jika file dan laporan SHA-256 sudah terverifikasi. Output final dua episode belum dibuat. Transkripsi lokal memakai ../.venv dan ../scripts/transcribe.py; model multilingual small belum dapat diunduh karena kebijakan jaringan. Model Bahasa Inggris saja tidak sesuai.

## Alur ekspor final

- Data editorial: ../docs/edit-plan.json dan src/data/pages.json.
- Timeline kedua episode: src/Episodes.tsx. Motion graphics: Opening.tsx, PartCard.tsx, Closing.tsx.
- CaptionTrack.tsx menggunakan tipe Caption JSON Remotion dan pengelompokan tampilan yang sama dengan eksportir ASS.
- Audio master olahan dibuat oleh `bash ../scripts/normalize_audio.sh` dari root proyek FTI-SIDE (skrip menetapkan direktori sendiri).
- `python ../scripts/export_episodes.py --part 1` dan `--part 2` dari folder mana pun mengekspor bagian percakapan, menanamkan subtitle, dan menggabungkan aset Remotion. Aset opening, kartu, teaser dan closing perlu dirender dari Studio terlebih dahulu seperti pendaftaran komposisinya.
- `python ../scripts/verify_deliverables.py` memeriksa format, durasi, jumlah frame dan decode penuh. `../.venv/bin/python ../scripts/check_audio_alignment.py` memeriksa kecocokan waveform audio pada enam posisi timeline.
- `python ../scripts/package_project.py` membuat arsip source. Arsip tidak menyertakan footage, node_modules, virtualenv, audio master olahan atau model ML. Gunakan sumber Drive di ../docs/SOURCES.md dan skrip yang disertakan untuk mereproduksi aset besar.

Perintah awal README merujuk studi desain pertama. Komposisi final editing tersedia sebagai FTI-SIDE-PART-1 dan FTI-SIDE-PART-2. Subtitle berbasis ASR dengan koreksi terpilih; lihat catatan keterbatasan bahasa pada README hasil.
