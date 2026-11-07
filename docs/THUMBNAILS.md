# Thumbnail Episode 1 Part 1 — foto asli

Kedua thumbnail memakai satu frame dari opening.mp4 pada detik 48.0. Source JPEG disimpan di studio/public/images/thumbnail-ep1-original-source.jpg. Semua peserta tetap dalam satu foto; tidak ada generative AI, rekonstruksi wajah, face retouch, atau pemisahan/penggambaran ulang peserta. Python/Pillow hanya menambahkan tipografi, garis, badge dan latar. Foto grup vertikal ditampilkan utuh dengan resize; versi horizontal mempertahankan resolusi frame 1920×1080. Latar dekoratif vertikal merupakan blur dari foto yang sama. Area wajah pada foto utama tidak diberi filter.

Hasil:
- deliverables/thumbnails/FTI-SIDE-EP1-PART1-HORIZONTAL.png — 1920×1080.
- deliverables/thumbnails/FTI-SIDE-EP1-PART1-VERTIKAL.png — 1080×1920.

Reproduksi: python scripts/make_original_thumbnails.py. Versi ini menggantikan thumbnail hasil generasi sebelumnya sesuai permintaan pengguna.

## Episode 1 Part 2

Horizontal 1920×1080 dan vertikal 1080×1920 memakai satu frame asli podcast.mp4 pada source 2275.0 detik (momen bye-bye Part 2). Judul Bertumbuh Bareng dengan badge EP 01 / PART 2, warna/font selaras Part 1. Empat peserta tetap dalam satu foto tanpa generative AI/retouch wajah. File PNG dan JPEG tersedia di deliverables/thumbnails/FTI-SIDE-EP1-PART2-{HORIZONTAL,VERTIKAL}. Reproduksi: python scripts/make_part2_thumbnails.py. JPEG disediakan agar ukuran nyaman untuk unggahan thumbnail.

## Versi AI Part 2

Atas permintaan terbaru pengguna, tersedia desain AI terpisah: FTI-SIDE-EP1-PART2-AI-HORIZONTAL.png dan FTI-SIDE-EP1-PART2-AI-VERTIKAL.png. Dibuat dengan image_gen memakai frame asli source 2275.0 sebagai referensi empat peserta; versi vertikal juga memakai desain horizontal sebagai acuan. Desain navy/oranye, torn-paper dan rim lighting, judul Bertumbuh Bareng. Wajah merupakan hasil olahan AI. Versi foto asli tetap tersedia.
