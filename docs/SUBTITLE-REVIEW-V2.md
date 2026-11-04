# Pemeriksaan subtitle revisi 2

Versi awal MP4, Caption JSON, halaman subtitle, SRT dan laporan QC disimpan di revisions/v1 sebelum perubahan.

27 potongan audio diproses ulang secara lokal dengan model multilingual large-v3-turbo. Hasilnya dibandingkan dengan transkripsi sebelumnya; hasil menyimpang, termasuk ucapan penutup generik yang muncul pada potongan 08:40–08:49, tidak dipakai.

Perubahan yang diterapkan:
- 59 koreksi ejaan, nama yang telah dikonfirmasi, istilah dan penanda ucapan/nama yang belum jelas, serta pemulihan dialog pada akhir rekaman.
- 118 perbaikan penulisan kata ulang, akhiran, singkatan dan angka/jam tanpa menggeser timestamp sumber.
- Ucapan follow/like/komen/subscribe sekitar source 37:24–37:30 dipulihkan dengan timestamp per kata dan confidence tinggi dari transkripsi lokal.
- 1.109 halaman subtitle diperiksa: durasi positif dan tidak ada halaman tumpang tindih. ESLint dan TypeScript lulus.

Jejak perubahan: subtitle-review-corrections.json dan subtitle-formatting-corrections.json. Hasil pengenalan per potongan berada di docs/subtitle-review. Skrip reproduksi: apply_subtitle_review.py, refine_caption_formatting.py, prepare_captions.py, write_transcript_outputs.py.

Ini adalah pemeriksaan teks dan perbandingan pengenalan suara, bukan peninjauan manual oleh manusia atas seluruh audio. Ucapan yang tetap ambigu dipertahankan dengan penanda, tanpa menebak kata atau identitas. Akurasi sempurna tidak diklaim.

Durasi, footage, urutan bahasan, titik cut, opening, musik dan closing tetap memakai timeline yang telah diverifikasi sebelumnya. Ekspor ulang diperlukan karena subtitle tertanam pada gambar video. QC teknis harus dilakukan lagi pada file revisi; laporan versi awal tidak membuktikan ekspor revisi sudah valid.
