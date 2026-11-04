# Part 1 V3 selesai; Part 2 tetap V2

Revisi mengikuti 63 butir permintaan pengguna. Part 1 1132.4 detik, 33972 frame, Full HD H.264/AAC stereo. Decode penuh lulus; enam titik audio cocok dengan lag sekitar 13.4 ms dan korelasi 0.986–0.997. Trailer Story 30 detik, 1080×1920, 900 frame, decode lulus. Lint/TypeScript lulus.

Foto Kak Aisyah dan screenshot paper mob dari tautan pengguna sudah digunakan. Opening memakai take baru dan musik baru; title episode transparan, perkenalan zoom, quote highlight, reset percakapan dipotong dengan dissolve AV, serta outro ilustrasi pause di atas podcast. Subtitle Part 1 tersendiri dan tidak memuat penanda kurang jelas. Rencana dan checklist pada docs/revision-v3. QC terbaru: deliverables/PART-1-V3-QC.json.

Part 2 identik byte demi byte dengan commit sebelumnya (SHA-256 pada docs/revision-v3/part2-preserved.json). Cadangan Part 1 sebelumnya ada di revisions/pre-user-part1-v3. Riwayat V2 di bawah tetap dipertahankan sebagai dokumentasi.

# FTI SIDE — revisi subtitle V2 selesai

## Video hasil revisi

- FTI-SIDE-PART-1.mp4: 1178.321 detik, 1324582892 byte, 35349 frame; decode penuh lulus.
- FTI-SIDE-PART-2.mp4: 1111.721 detik, 1571855500 byte, 33351 frame; decode penuh lulus.

Kedua video: Full HD 1920×1080, 30 fps, H.264 yuv420p BT.709, AAC stereo 48 kHz, subtitle tertanam. Audio cocok pada enam titik dengan lag sekitar 21,3 ms dan korelasi 0,977–0,995. Preview kedua episode diperbarui dari versi revisi.

## Revisi yang dilakukan

27 potongan audio diperiksa ulang secara lokal. 59 koreksi bahasa/penanda dan 118 perbaikan format diterapkan, termasuk penggabungan kata ulang, akhiran, angka/jam dan pemulihan ucapan follow/like/komen/subscribe yang terlewat. Data subtitle: 1.109 halaman dengan durasi positif dan tanpa tumpang tindih. Lint dan TypeScript lulus. Catatan lengkap di SUBTITLE-REVIEW-V2.md dan JSON audit.

Tiga titik tetap diberi penanda ucapan/nama kurang jelas; timestamp sumber dan episode pada deliverables/POTONGAN-PERLU-DICEK.csv. Ini tetap subtitle berbasis ASR dengan pemeriksaan terpilih, bukan jaminan peninjauan manusia atas setiap kata audio. Jangan mengarang kata atau nama yang belum jelas.

## Versi dan proyek

Versi awal MP4, proyek ZIP, subtitle, Caption JSON dan laporan QC dicadangkan di revisions/v1. Hasil terbaru berada di deliverables dengan nama yang sama seperti permintaan pengguna. Transkrip dan SRT sudah diperbarui. Arsip source baru dibuat dengan scripts/package_project.py.

Project Remotion berada di studio; gunakan npm run dev untuk Studio. Opening dan closing memakai grafis Remotion, isi clean menggunakan source asli. Edit-plan.json, EPISODE-NOTES.md dan EDIT-TIMESTAMPS.csv menyimpan pemetaan seluruh klip. Musik ident dibuat khusus tanpa sampel pihak ketiga.

Source asli tetap ada di studio/public/sources dan sudah terverifikasi; jangan diunduh ulang. Nama peserta: Nadya, Ghivariel, Kinan, Cahaya. FTI SIDE identitas utama; Kabinet ARKA disebut lewat tipografi tanpa menggambar ulang logo.

Empat frame ditahan pada ujung Part 2 karena video sumber berakhir lebih cepat dari audio. Untuk ekspor ulang, tpad ditempatkan sebelum trim sumber; uji EOF dua detik menghasilkan tepat 60 frame.

Gunakan checkout terisolasi yang sudah ada; jangan membuat Git worktree kecuali diminta. Tidak ada publikasi atau penerapan ulang konfigurasi environment pada tahap revisi ini.
