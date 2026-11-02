# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program berbasis Python yang dirancang untuk membantu guru dalam mengolah nilai matematika siswa secara lebih mudah dan sistematis.

Program ini dapat membaca data nilai siswa dari file teks, memvalidasi data, menghitung statistik nilai, menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil analisis ke dalam file laporan.

## 2. Tujuan Proyek

1. Mempermudah proses rekapitulasi nilai matematika siswa.
2. Membantu guru menghitung statistik nilai secara otomatis.
3. Menentukan status ketuntasan siswa berdasarkan KKM.
4. Mengurangi kesalahan dalam pengolahan nilai.
5. Menghasilkan laporan nilai yang mudah dibaca.

## 3. Fitur Program

- Membaca data nilai siswa dari file teks.
- Memvalidasi format data dan rentang nilai 0–100.
- Menghitung jumlah siswa dan total nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menentukan status tuntas atau belum tuntas.
- Menghitung persentase ketuntasan.
- Menyimpan laporan hasil analisis ke file teks.

## 4. Persyaratan Sistem

- Python 3.x
- Visual Studio Code
- Git
- Sistem operasi yang mendukung Python.

Program menggunakan modul bawaan Python sehingga tidak memerlukan instalasi library tambahan.

## 5. Struktur Folder

```text
proyek-akhir-rekap-analisis-nilai/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   ├── test_program.py
│   └── bug_log.md
└── output/
    └── .gitkeep
```

## 6. Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka folder proyek melalui Visual Studio Code.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah:

```bash
python src/main.py
```

5. Masukkan nilai KKM ketika diminta.
6. Program akan menampilkan hasil analisis dan menyimpan laporan ke folder output.

## 7. Format Data Masukan

Data siswa disimpan dalam file `nilai_contoh.txt` dengan format:

```text
Nama Siswa,Nilai
Andi,80
Budi,70
Citra,90
```

Nilai harus berupa angka dalam rentang 0 sampai 100.

## 8. Pengujian Program

Pengujian dilakukan menggunakan modul unittest dan pengujian manual.

Pengujian mencakup:
- Data normal.
- Nilai batas bawah dan batas atas.
- Input bukan angka.
- Nilai di luar rentang.
- Data kosong.
- File tidak ditemukan.
- Penentuan status ketuntasan.

Untuk menjalankan pengujian otomatis:

```bash
python -m unittest discover -s tests -v
```

Hasil pengujian dicatat dalam `tests/test_case.md`.

## 9. Known Issues

Masalah yang masih diketahui:
- Program menggunakan file teks dengan format nama dan nilai yang dipisahkan tanda koma.
- Program belum menyediakan antarmuka grafis.
- Program belum memiliki fitur penyimpanan ke database.

## 10. Anggota dan Kontribusi

| Anggota | Kontribusi |
|---|---|
| Nama Anggota 1 | Koordinator proyek |
| Nama Anggota 2 | Pengembangan pengolahan data |
| Nama Anggota 3 | Pengembangan logika analisis |
| Nama Anggota 4 | Pengujian dan debugging |
| Nama Anggota 5 | Dokumentasi proyek |

*Sesuaikan nama dan pembagian kontribusi dengan anggota kelompok yang sebenarnya.*

## 11. Referensi dan Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14.
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 15.
- Python Software Foundation, Python 3 Documentation.
- Dokumentasi Visual Studio Code.
- Dokumentasi Git dan GitHub.
- Bantuan AI digunakan untuk mendukung penyusunan dan pemeriksaan kode. Setiap kode ditinjau dan diuji kembali oleh anggota proyek.

## 12. Penutup

Program ini diharapkan dapat membantu proses pengolahan nilai matematika siswa menjadi lebih praktis, terstruktur, dan efisien. Pengembangan selanjutnya dapat dilakukan dengan menambahkan fitur sesuai kebutuhan pengguna.
