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

Kode proyek, transkrip lengkap, SRT, catatan editing dan laporan QC tersedia di repository ini. Kedua MP4 final masing-masing lebih dari 1 GB, sehingga direncanakan sebagai aset **GitHub Releases**, bukan blob Git biasa. **Upload video ke Releases belum selesai.**

- [Transkrip lengkap](deliverables/TRANSKRIP-LENGKAP.txt)
- [Catatan episode](deliverables/CATATAN-EPISODE.md)
- [Catatan revisi subtitle V2](deliverables/CATATAN-SUBTITLE-V2.md)
- [QC teknis](deliverables/QC-REPORT.json)
- [Tiga titik yang masih perlu konfirmasi](deliverables/POTONGAN-PERLU-DICEK.csv)

Kedua video final telah lolos decode penuh H.264 Full HD/AAC stereo. Subtitle berbasis Whisper dengan koreksi terpilih; beberapa ucapan/nama tetap diberi penanda, tanpa mengarang kata pengganti.

## Aset besar

Footage mentah, master audio olahan, model transkripsi, dependencies, cache render dan cadangan MP4 tidak dimasukkan ke Git. Footage tetap tersedia di lingkungan cloud. Lokasi sumber dan metadata: [docs/SOURCES.md](docs/SOURCES.md). Musik ident original proyek disertakan; asalnya dijelaskan di [docs/MUSIC-PROVENANCE.md](docs/MUSIC-PROVENANCE.md).
