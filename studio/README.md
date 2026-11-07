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

## Revisi Part 1 V3

Part 1 memakai `Part1RevisionV3.tsx` dan data caption terpisah agar Part 2 tetap sama. Rencana potongan: `docs/revision-v3/plan.json`. Foto pengguna berada di `public/images`; musik dan efek baru dibuat oleh `scripts/make_part1_music_v3.py`.

Dari akar repository:

```sh
python scripts/prepare_part1_user_revision_v3.py
python scripts/make_part1_music_v3.py
cd studio
npx remotion render Part1-Opening-V3 ../renders/part1-opening-v3.mp4 --browser-executable=/usr/bin/chromium
npx remotion render Part1-Pause-Outro-V3 ../renders/part1-outro-v3.mp4 --browser-executable=/usr/bin/chromium
npx remotion render Part1-Instagram-Story-V3 ../deliverables/FTI-SIDE-PART-1-STORY.mp4 --browser-executable=/usr/bin/chromium
cd ..
python scripts/export_part1_user_revision_v3.py
python scripts/qc_part1_v3.py
```

Master sumber dan normalized main audio tidak dikemas ke Git. Opening normalized WAV disertakan. Export V3 menghasilkan nama sementara `FTI-SIDE-PART-1-V3.mp4`; setelah QC, salin ke nama final `FTI-SIDE-PART-1.mp4`.


## Revisi Part 1 dan Story V4

Komposisi pada file Part1RevisionV3.tsx/Part1StoryV3.tsx sudah mencakup revisi V4. Render opening ke `renders/part1-opening-v4.mp4` dan Story ke `renders/part1-story-v4.mp4`, lalu jalankan `python scripts/export_part1_user_revision_v4.py` dan `python scripts/qc_part1_v4.py`. Sesudah QC, salin MP4 sementara ke nama final di deliverables. Rencana dan timing foto terbaru pada docs/revision-v4/plan.json. Subtitle dan durasi episode tetap V3.


## Episode 1 Part 2 — revisi V3

Komposisi baru pada Part2RevisionV3.tsx: Part2-Intro-V3 (600 frame), Part2-Outro-V3 (300), Part2-Story-V3 (960), dan FTI-SIDE-PART-2 (33429). Subtitle khusus Part 2 berada di data/part2-pages-v3.json. Rencana, dokumentasi sumber dan alur reproduksi lengkap: ../docs/part2-revision-v3/notes.md. Ekspor penuh memakai scripts/export_part2_revision_v3.py; uji format/sinkronisasi scripts/qc_part2_revision_v3.py.


## Trailer Part 2 V4

ID komposisi tetap Part2-Story-V3, durasi kini 720 frame (24 detik). Render terbaru ke renders/part2-story-v4.mp4. Throwback 2 detik grayscale, close-up pembicara bergantian, wide pada respons bersama dan penutup empat kata. Video utama tetap V3. Detail: ../docs/STORY-PART-2-V4.md.

## Part 2 dan trailer V5

Komposisi tetap pada Part2RevisionV3.tsx. Data aktif part2-pages-v5.json/part2-plan-v5.json, helper Part2PlaybackV5.tsx. Intro 600 frame, outro 300, Story kini 810 (27 detik), utama 33429. Musik/rewind original: scripts/make_part2_music_v5.py. Render intro/outro/story ke renders/part2-{intro,outro,story}-v5.mp4 lalu scripts/export_part2_revision_v5.py dan scripts/qc_part2_revision_v5.py. Catatan lengkap: ../docs/part2-revision-v5/notes.md. Setelah QC, salin hasil sementara ke nama unduhan canonical.
