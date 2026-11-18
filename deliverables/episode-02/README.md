# FTI SIDE · Episode 02

**KITA BENERAN GAPAPA, ATAU UDAH KEBIASA AJA?**

- [Part 1 · 14:24 (MP4)](FTI-SIDE-EP02-PART-1.mp4) mengikuti obrolan tentang rasa capek, perubahan kecil yang terasa, dan kapan mereka siap bercerita.
- [Part 2 · 17:29 (MP4)](FTI-SIDE-EP02-PART-2.mp4) mulai dari pertanyaan tentang ekspektasi dan rasa takut tertinggal. Obrolan diteruskan hingga pesan dan salam penutup.
- Subtitle Indonesia tertanam di kedua video. Berkas SRT disertakan untuk koreksi dan aksesibilitas.

Titik pisah ada pada 00:14:08,930 di sumber, di jeda sebelum moderator membuka bahasan baru. Part 2 memakai cuplikan Part 1 dalam grayscale sebelum kartu judul. Tipografi krem, aksen oranye, identitas di kiri atas, dan subtitle di bawah mengikuti Episode 1. Cue pop 96 BPM dibuat dari piano elektrik, pad, bas, dan perkusi sintesis tanpa rekaman pihak ketiga. Musik mengiringi grafis pembuka dan penutup. Dialog diberi filter dan kompresi ringan, dengan target normalisasi −16 LUFS.

Subtitle berasal dari transkripsi otomatis bahasa Indonesia yang dirapikan dengan pengelompokan maksimal dua baris dan koreksi terpilih. Bagian yang sulit dipahami, seperti percakapan bertumpuk, bisa memiliki celah subtitle.

## Render ulang

Dari direktori ini, simpan footage Drive sebagai `source.mp4`. Dibutuhkan FFmpeg dengan libass dan libx264, font DejaVu Sans, serta Python dengan NumPy.

```sh
ffmpeg -i source.mp4 -vn -af 'highpass=f=72,lowpass=f=13500,acompressor=threshold=0.16:ratio=2.3:attack=10:release=180:knee=2.2:link=maximum:detection=rms,loudnorm=I=-16:TP=-1.5:LRA=10,aresample=48000' -c:a pcm_s16le voice.wav
python make_music.py
python edit_episode.py 1
python edit_episode.py 2
```

File `edit-plan.json` memakai detik dalam footage asli. File `captions.json` berisi cue pada waktu sumber. Saat merevisi potongan atau subtitle, render ulang klip yang terdampak dengan memindahkan hasil lama dari folder render `part1` atau `part2`. Raw footage tetap di Drive. [Unduh footage sumber](https://drive.google.com/file/d/1wZea8PiY__7rOWSAJtPO70j0TuUNo-3p/view)
