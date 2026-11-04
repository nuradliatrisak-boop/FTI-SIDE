# Pemeriksaan setelah publish

- Aturan drive.google.com dan drive.usercontent.google.com aktif pada instance baru.
- Sumber podcast utama: endpoint download dengan confirm=t merespons video/mp4 (sekitar 1,2 GB). Unduhan dimulai; lihat berkas sumber dan metadata untuk hasil akhir.
- Sumber opening: halaman view HTTP 401; endpoint download dengan confirm=t mengarah ke accounts.google.com/ServiceLogin. Memerlukan akses publik atau tautan pengganti. Jangan mencoba mengganti footage dengan peserta palsu.
- faster-whisper terpasang di ../.venv; impor berhasil. Tidak ada model lokal sebelumnya. Endpoint model Hugging Face ditolak proxy (HTTP 403).
- Draft baru menambahkan huggingface.co dan cas-bridge.xethub.hf.co, mempertahankan dua domain Drive. Belum diterapkan atau dipublish oleh agen.
- Transkripsi belum dimulai. scripts/transcribe.py menghasilkan transkrip draf dan Caption JSON dengan timestamp sumber; wajib ditinjau sebelum subtitle final.
- Studio telah dimulai kembali dan HTTP lokal merespons.
