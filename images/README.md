Taruh di sini:
- profile.jpg        -> foto profil (dipakai di hero)
- screenshot-1.png    -> Exhibit A (section id="gallery" — current build)
- screenshot-2.png    -> Exhibit B
- screenshot-3.png    -> Exhibit C
- screenshot-4.png    -> Exhibit D

Sebelum file-file ini ada, index.html otomatis nampilin kotak placeholder (bukan icon broken image).

## v87/

10 screenshot untuk section id="gallery-v87" (Exhibit A–J, build v87 — versi yang dipakai 2 junior lulus ujian). File JPEG di-recompress quality 85 tanpa resize (tetap resolusi asli, biar teks Jepang/angka masih kebaca kalau di-expand); 2 file .webp dibiarkan format asli karena sudah lebih efisien dari re-encode JPEG.

Semua foto di kedua gallery ("gallery" dan "gallery-v87") bisa diklik untuk expand ke lightbox (tombol × atau klik luar buat nutup) — script-nya nempel di akhir index.html, jalan otomatis ke tiap `.gallery-frame` yang ada, jadi nambah figure baru di gallery manapun otomatis ikut punya fitur expand ini.
