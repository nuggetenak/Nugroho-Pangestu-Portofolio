# Portfolio — Nugroho Pangestu

Portofolio satu halaman (`index.html`), siap deploy ke GitHub Pages. Sudah ada slot foto profil (kotak placeholder bergaris kalau file belum ada — bukan ikon broken image), plus dua section Exhibit: build v4.23.0 yang lagi aktif dikembangkan (8 screenshot, A–H) dan build v87 yang frozen — versi yang dipakai 2 junior lulus ujian (10 screenshot, A–J). Semua foto exhibit bisa diklik buat expand (lightbox, tutup pakai tombol × / klik luar / Esc).

## Struktur folder di repo

```
nuggetenak.github.io/
├── index.html
└── images/
    ├── profile.jpg        ← foto kamu
    ├── v423/               ← screenshot build v4.23.0 (Exhibit A–H, section id="gallery-v423")
    │   ├── v423-01-beranda.jpg
    │   ├── ...
    │   └── v423-08-saya-progres.jpg
    └── v87/                ← screenshot build v87 (Exhibit A–J, section id="gallery-v87")
        ├── v87-01-belajar-overview.jpg
        ├── ...
        └── v87-10-progres.jpg
```

Nama file di atas harus persis sama — kalau mau ganti nama, tinggal cari-ganti path-nya di `index.html` (cari `src="images/...`). Butuh lebih/kurang screenshot di section manapun? Blok `<figure class="gallery-item">...</figure>` di section `id="gallery-v423"` (build v4.23.0) atau `id="gallery-v87"` (build v87) tinggal copy-paste atau hapus — foto baru otomatis ikut kena fitur expand-to-lightbox, tidak perlu wiring tambahan.

## Deploy ke GitHub Pages

Cek dulu: akun **nuggetenak** belum punya repo `nuggetenak.github.io` — nama ini yang bikin URL-nya bersih (`https://nuggetenak.github.io/`, tanpa embel-embel nama repo).

1. Buat repo baru di GitHub, nama persis: `nuggetenak.github.io`
2. Dari Termux:
   ```bash
   git clone https://github.com/nuggetenak/nuggetenak.github.io.git
   cd nuggetenak.github.io
   mkdir images
   # taruh profile.jpg + folder v423/ + folder v87/ ke folder images/ di sini
   cp /path/ke/index.html .
   git add .
   git commit -m "portfolio v1"
   git push
   ```
   (Belum ada foto/screenshot? Push aja dulu tanpa isi folder `images/` — placeholder-nya tetap tampil rapi. Tinggal `git add images/*.jpg images/*.png && git commit -m "add photos" && git push` kapan pun file siap.)
3. Settings → Pages di repo itu → pastikan **Source: Deploy from branch: main / (root)**. Situs live dalam 1-2 menit di `https://nuggetenak.github.io/`.

Alternatif tanpa terminal: buat repo di atas lewat browser, klik **Add file → Upload files**, drag `index.html` + folder `images/` langsung dari HP.
