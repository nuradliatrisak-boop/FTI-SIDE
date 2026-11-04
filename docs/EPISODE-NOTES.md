# Pembagian episode FTI SIDE

Nama dikonfirmasi pengguna: Nadya, Ghivariel, Kinan, Cahaya.

## Part 1 — Kenapa Ikut Organisasi?
Sumber utama 00:03,800–19:21,600. Mempertahankan perkenalan, obrolan spontan, alasan bergabung, ekspektasi dan realita, relasi, serta pengalaman baru. Titik akhir berada sesudah rangkaian pengalaman dan sebelum pertanyaan baru tentang perubahan diri. Bukan pembagian berdasarkan setengah durasi.

Urutan output: opening Remotion 16 detik; kartu Part 1 selama 4 detik; percakapan 19:06,300; teaser tipografi Part 2 selama 5 detik; closing 7 detik. Target 19:38,300.

## Part 2 — Bertumbuh, Memimpin, Mengatur Waktu
Sumber utama 19:21,600–37:59,900. Pertanyaan pembuka merangkum bahasan sebelumnya dan mengalihkan fokus ke perubahan diri. Dilanjutkan kepemimpinan program kerja, prioritas akademik, istirahat, pesan untuk mahasiswa, dan penutup asli.

Urutan output: opening yang sama 16 detik; kartu Part 2 selama 4 detik; percakapan 18:04,700; closing 7 detik. Target 18:31,700.

## Keputusan editing
- Hapus persiapan rekam/hitungan 00:00,000–00:03,800, diskusi melakukan cut pada 09:55,600–10:07,100, serta diskusi teknis memilih pertanyaan pada 31:13,600–31:47,200. Semua batas dipilih pada jeda ujaran.
- Pertahankan seluruh bahasan utama berikutnya, urutan percakapan, spontanitas, candaan dan reaksi asli. Tidak mempercepat percakapan.
- Tidak memotong jeda semata-mata karena deteksi otomatis: analisis tidak menemukan hening >=1,5 detik di -35 dB. Tidak ada dasar aman untuk membuang percakapan lain secara agresif.
- Isi memakai wide shot natural, identitas kecil di pojok kiri atas, subtitle tetap di area bawah meja. Tidak memakai zoom atau transisi berulang.
- Audio stereo dinormalisasi ke sekitar -16,45 LUFS dan true peak -1,5 dBTP; tidak ada musik sepanjang percakapan.
- Opening adalah desain Remotion khusus dengan montage footage opening asli, crop, split screen, kinetic typography dan musik instrumental original proyek. Audio montage dimatikan agar potongan percakapan tidak disusun ulang menjadi ucapan palsu.
- Closing memakai tipografi FTI SIDE / BEM FTI Universitas Trisakti / Kabinet ARKA. Logo resmi tidak digambar ulang; berkas gambar dari chat belum tersedia sebagai aset lokal.

## Reproduksi
Komposisi lengkap kedua episode tersedia di studio/src/Episodes.tsx. Caption JSON dan edit-plan.json adalah sumber data subtitle dan timeline. Motion graphics dirender dengan Remotion. scripts/export_episodes.py menggunakan FFmpeg untuk encode bagian percakapan yang clean, menanamkan subtitle dari data yang sama, menyamakan ruang warna/timebase, dan menggabungkan grafis Remotion tanpa encode ulang seluruh film lewat Chromium.

Pemeriksaan otomatis dan visual tidak setara dengan peninjauan manusia atas setiap kata audio. Simpan draf ASR dan catatan koreksi agar revisi dapat ditelusuri.
