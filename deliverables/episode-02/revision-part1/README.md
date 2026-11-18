# Episode 2 Part 1 · Revisi 2

Bumper baru menggunakan empat potongan footage Episode 2 dan judul episode. Perkenalan asli dipindah ke depan, dari footage sekitar 03:24 sampai sambutan grup di 03:39. Fajar, Fathur, Chiaro, Kinan, dan Muti mendapat crop tersendiri dengan kartu nama. Percakapan sumber dari 00:04,930 sampai 03:24,100 tetap masuk setelah sambutan. Isi utama lanjut dari 03:39 sampai titik pisah asli 14:08,930.

Subtitle direvisi di waktu sumber dengan koreksi ucapan dari pengguna, terutama pertanyaan Fajar, penjelasan Chiaro, tanggapan Fathur, dan cerita PKKMB Kinan. Tempo subtitle mengikuti awal dan akhir frasa. Dialog yang bertumpuk dan sulit dibedakan masih menyisakan beberapa jeda subtitle.

Trailer 9:16 memakai satu cuplikan dialog dari masing-masing pembicara. Musiknya instrumental indie-pop orisinal 108 BPM dengan petikan sintetis, perkusi ringan, dan pad. Desain teks pojok kiri video utama mengulang setelan persis dari skrip ekspor Episode 1 Part 1 V4.

## Render ulang

Siapkan `source.mp4` dan `voice.wav` di direktori ini. Gunakan perintah pada README Episode 2 untuk membuat master `voice.wav`. Dibutuhkan FFmpeg dengan libass, libx264, dan drawtext, serta Python dengan NumPy dan font DejaVu Sans.

```sh
python make_music_r2.py
python render_r2.py main
python render_r2.py trailer
```

Video utama tersedia di folder render `r2/`, dan trailer di `story/`. Tiap output disertai SRT. Cue pada `captions-r2.json` memakai waktu sumber. Saat mengganti cue atau crop, pindahkan klip render yang terdampak agar skrip merendernya kembali.
