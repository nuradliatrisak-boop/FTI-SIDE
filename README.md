# FTI SIDE — BEM FTI Universitas Trisakti

Project editing podcast dengan Remotion: opening motion graphics, dua episode, subtitle, audio stereo dan closing.

## Menjalankan proyek

Gunakan Node.js 24 dan checkout ini. Setiap task cloud sudah terisolasi; tidak perlu membuat Git worktree baru.

```sh
cd studio
npm ci
npm run dev
```

Komposisi `FTI-SIDE-PART-1` berdurasi sekitar 19:38; `FTI-SIDE-PART-2` sekitar 18:32. Penjelasan teknis dan ekspor: [studio/README.md](studio/README.md).

## Hasil dan unduhan

Kedua MP4 final revisi subtitle V2 telah diunggah melalui **Git LFS**. Buka tautan GitHub di bawah dan gunakan unduhan file dari GitHub.

- [Unduh Part 1 — 19:38](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-PART-1.mp4)
- [Unduh Part 2 — 18:32](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-PART-2.mp4)
- [Arsip proyek Remotion](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-REMOTION-PROJECT.zip)

Untuk clone lokal, pasang Git LFS sebelum menjalankan `git clone`, kemudian jalankan `git lfs pull` jika video masih berupa pointer.

- [Transkrip lengkap](deliverables/TRANSKRIP-LENGKAP.txt)
- [Catatan episode](deliverables/CATATAN-EPISODE.md)
- [Catatan revisi subtitle V2](deliverables/CATATAN-SUBTITLE-V2.md)
- [QC teknis](deliverables/QC-REPORT.json)
- [Tiga titik yang masih perlu konfirmasi](deliverables/POTONGAN-PERLU-DICEK.csv)

Kedua video final telah lolos decode penuh H.264 Full HD/AAC stereo. Subtitle berbasis Whisper dengan koreksi terpilih; beberapa ucapan/nama tetap diberi penanda, tanpa mengarang kata pengganti.

## Aset besar

Footage mentah, master audio olahan, model transkripsi, dependencies, cache render dan cadangan MP4 tidak dimasukkan ke Git. Footage tetap tersedia di lingkungan cloud. Lokasi sumber dan metadata: [docs/SOURCES.md](docs/SOURCES.md). Musik ident original proyek disertakan; asalnya dijelaskan di [docs/MUSIC-PROVENANCE.md](docs/MUSIC-PROVENANCE.md).
