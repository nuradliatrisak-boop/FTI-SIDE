# Trailer Story V6 selesai

Judul “24 JAM NGGAK CUKUP?” dengan aksen oranye. Teks masuk bertahap, spring, underline, sapuan transisi, gerak kamera dan efek suara pendek. Fokus Kinan dan welcome empat peserta dipertahankan. 30 detik, 900 frame, 1080×1920 H.264/AAC stereo; decode penuh dan lint/TypeScript lolos. Audio -15.33 LUFS, true peak -1.14 dBTP, tanpa clipping. QC: deliverables/STORY-V6-QC.json. Riwayat di bawah.

# Trailer Story V5 selesai

Crop bagian “Pusing? Ada asiknya juga!” detik 13–19.3 dibetulkan ke Kinan (jaket cokelat). Frame hasil detik 16 diperiksa. Trailer 30 detik, 900 frame, 1080×1920 H.264/AAC stereo; decode penuh dan lint/TypeScript lolos. QC: deliverables/STORY-V5-QC.json. Part 1 dan Part 2 tidak diubah. Riwayat di bawah.

# Part 1 dan Story V4 selesai

Judul opening “Ikut Ormawa, Ikut Pusing?” dan “Kehidupan Ormawa FTI”. Arah zoom Ghivariel/Kinan dibetulkan sesuai pengguna. Foto Kak Aisyah source 101.8–103.3; paper mob 1090–1095, telah diperiksa pada frame hasil final sebelum dan sesudah batas tampil.

Trailer 30 detik tanpa handle, klip organisasi menggantikan deg-degan, welcome seluruh frame empat peserta, CTA “Saksikan FTI SIDE selengkapnya!”, dissolve gambar dan fade audio. Visual trailer diperiksa pada detik 1.5, 21, dan 26.

Part 1 1132.4 detik, 33972 frame, H.264 Full HD/AAC stereo; decode penuh lolos, sinkronisasi enam titik lag ~13.4 ms, korelasi 0.986–0.997. Story 1080×1920, 900 frame, decode lolos. Lint/TypeScript lolos. QC terbaru deliverables/PART-1-V4-QC.json. Subtitle dan Part 2 tetap sama; SHA-256 Part 2 cocok dengan commit sebelumnya. Cadangan lokal V3 di revisions/pre-user-part1-v4. Catatan di bawah adalah riwayat.

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
