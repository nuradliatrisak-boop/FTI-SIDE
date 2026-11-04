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
