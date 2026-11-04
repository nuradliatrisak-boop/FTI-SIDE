# FTI SIDE — BEM FTI Universitas Trisakti

Project editing podcast dengan Remotion: opening motion graphics, dua episode, subtitle, audio stereo dan closing.

## Menjalankan proyek

Gunakan Node.js 24 dan checkout ini. Setiap task cloud sudah terisolasi; tidak perlu membuat Git worktree baru.

```sh
cd studio
npm ci
npm run dev
```

Komposisi `FTI-SIDE-PART-1` berdurasi sekitar 18:52; `FTI-SIDE-PART-2` sekitar 18:32. Penjelasan teknis dan ekspor: [studio/README.md](studio/README.md).

## Hasil dan unduhan

Part 1 direvisi sesuai catatan pengguna (V3); Part 2 tetap versi V2. Video diunggah melalui **Git LFS**. Buka tautan GitHub di bawah dan gunakan unduhan file dari GitHub.

- [Unduh Part 1 — 18:52](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-PART-1.mp4)
- [Trailer Instagram Story — 30 detik](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-PART-1-STORY.mp4)
- [Unduh Part 2 — 18:32](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-PART-2.mp4)
- [Arsip proyek Remotion](https://github.com/nuradliatrisak-boop/FTI-SIDE/raw/refs/heads/main/deliverables/FTI-SIDE-REMOTION-PROJECT.zip)

Untuk clone lokal, pasang Git LFS sebelum menjalankan `git clone`, kemudian jalankan `git lfs pull` jika video masih berupa pointer.

- [Transkrip Part 1 revisi V3](deliverables/TRANSKRIP-PART-1-V3.txt)
- [Transkrip sumber lengkap](deliverables/TRANSKRIP-LENGKAP.txt)
- [Catatan episode](deliverables/CATATAN-EPISODE.md)
- [Catatan revisi subtitle V2](deliverables/CATATAN-SUBTITLE-V2.md)
- [QC Part 1 V3 dan Story](deliverables/PART-1-V3-QC.json)
- [QC versi sebelumnya / Part 2](deliverables/QC-REPORT.json)
- [Catatan ketidakjelasan sumber versi V2](deliverables/POTONGAN-PERLU-DICEK.csv)

Kedua video final telah lolos decode penuh H.264 Full HD/AAC stereo. Subtitle Part 1 diperbaiki mengikuti catatan pengguna; ucapan yang belum jelas dibiarkan tanpa subtitle. Part 2 masih mengikuti versi sebelumnya. Lihat [catatan revisi Part 1 V3](deliverables/CATATAN-PART-1-V3.md).

## Aset besar

Footage mentah, master audio olahan, model transkripsi, dependencies, cache render dan cadangan MP4 tidak dimasukkan ke Git. Footage tetap tersedia di lingkungan cloud. Lokasi sumber dan metadata: [docs/SOURCES.md](docs/SOURCES.md). Musik ident original proyek disertakan; asalnya dijelaskan di [docs/MUSIC-PROVENANCE.md](docs/MUSIC-PROVENANCE.md).
