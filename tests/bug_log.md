# BUG LOG
## Program Rekap dan Analisis Nilai Matematika

### BUG-01
Gejala:
Program berpotensi menerima nilai nan sebagai nilai valid.

Penyebab:
Validasi sebelumnya hanya memeriksa apakah nilai
berada di bawah 0 atau di atas 100.

Perbaikan:
Menambahkan math.isfinite() pada fungsi validasi_nilai().

Pengujian ulang:
Menjalankan test_nilai_nan dan test_nilai_normal.

Status:
Closed.

---

### BUG-02
Gejala:
Program dapat mengalami kesalahan pembagian dengan nol
ketika daftar nilai kosong.

Penyebab:
Perhitungan rata-rata dilakukan tanpa memeriksa
apakah daftar nilai memiliki data.

Perbaikan:
Menambahkan pemeriksaan daftar kosong sebelum
melakukan perhitungan statistik.

Pengujian ulang:
Menjalankan test_data_kosong.

Status:
Closed.