# Episode 1 • Part 2 — revisi pengguna V3

Identitas utama selaras dengan Part 1: oranye #ff8948, krem, footage nyata, caption di bawah dan label kiri atas (95,65). Label kini FTI SIDE / EP 1 • PART 2. Musik instrumental variasi baru 132 BPM dengan harmoni baru, masih dari keluarga suara ident orisinal Part 1.

## Timeline

- 0–8 detik: throwback percakapan Part 1 tentang alasan berorganisasi dan “Terbentur, terbentur, dan terbentuk”.
- 8–20 detik: montage opening baru, tema bertumbuh/proker/prioritas dan judul Part 2 di atas footage.
- Isi mulai 19.8 detik dengan dissolve gambar dan audio 0.2 detik.
- Source 1161.6–1873.6 lalu 1907.2–2279.9; sambungan internal memakai dissolve 0.2 detik.
- Montage penutup 10 detik, footage kelompok dan lambaian tangan asli, ajakan @bemftiusakti, tanpa kartu latar biru.

Rencana total 1114.3 detik (18:34.3), 33429 frame, Full HD 30 fps. Trailer vertikal 32 detik, 960 frame, throwback lalu cuplikan Part 2 dan CTA.

## Dokumentasi asli pengguna

- FTI Impact: source 1521.1–1529.1, saat Kinan menyebut scroll BEM FTI. https://drive.google.com/file/d/1Ri77kJph1DDPMd8yk8D4ZR-cOBeTLegq/view
- Studi Ekskursi/Sari Roti: source 1609.4–1617.4. https://drive.google.com/file/d/1MGPdDEwmRZDptORzXDtkqklzzmYy9p5t/view
- Upgrading/Skill Achievement: source 1645.4–1653.4. https://drive.google.com/file/d/1QPLxPDsq5ZmcbbdWtBPw5UJAw4q-v00Z/view

Ketiga screenshot ditampilkan utuh dalam kartu oranye/charcoal dengan judul proker dan @bemftiusakti. Tidak ada rekonstruksi/generasi wajah atau foto.

## Subtitle dan kutipan

Data Part 2 terpisah dari Part 1. Koreksi mengikuti daftar pengguna, termasuk Puya/Kak Puya, Ghivariel, fun fact, studi ekskursi, hectic, skill achievement, proker A, asbun, Just all out, sharing-sharing, tata krama. Dua bagian yang diminta dihapus dan penanda ucapan belum jelas tidak ditampilkan. Checklist mencatat 55 entri karena nomor 35 dipakai dua kali oleh pengguna.

Sepuluh highlight kutipan berbasis ucapan yang ada, tanpa mengubah suara atau mengatribusikan kalimat baru. Bagian pesan akhir menyorot confident/all out, tanggung jawab/tata krama, komitmen/time management, tiga pesan tentang progres dan hasil, serta “boleh kurang bensin, tapi jangan sampai habis bensin”.

## Dialog

Master Part 2 terpisah: high-pass 70 Hz, presence EQ ringan +1.5 dB pada 2700 Hz, kompresi lembut, dynaudnorm maksimum 2× dan loudnorm -16 LUFS/TP -1.5 dBTP. Pada lima jendela contoh lag master baru terhadap master lama ~-0.06 ms. Jendela source 1260 dan 1732 mendapat peningkatan RMS sekitar +2.35/+2.38 dB; dialog yang sudah kuat tidak dinaikkan sama rata. Tidak memakai clone suara. Lihat enhance_part2_audio.py.

## Reproduksi

1. python scripts/prepare_part2_revision_v3.py
2. python scripts/make_part2_music_v3.py
3. python scripts/enhance_part2_audio.py
4. Di studio, render Part2-Intro-V3 ke renders/part2-intro-v3.mp4, Part2-Outro-V3 ke renders/part2-outro-v3.mp4, Part2-Story-V3 ke renders/part2-story-v3.mp4. Gunakan --browser-executable=/usr/bin/chromium di cloud ini.
5. python scripts/export_part2_revision_v3.py
6. python scripts/qc_part2_revision_v3.py, decode penuh dan pemeriksaan visual.
7. Setelah QC, salin master V3 dan Story ke nama final yang dipakai di GitHub.

Part 1, trailer Part 1, dan thumbnail tetap versi yang telah disetujui. Footage sumber tidak perlu diunduh ulang.
