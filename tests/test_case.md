# HASIL PENGUJIAN PROGRAM

| ID | Fitur | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Rata-rata | 70, 80, 90 | 80 | 80 | PASS |
| TC02 | Nilai batas bawah | 0 | Diterima | Diterima | PASS |
| TC03 | Nilai batas atas | 100 | Diterima | Diterima | PASS |
| TC04 | Validasi nilai | 105 | Ditolak | Ditolak | PASS |
| TC05 | Validasi angka | abc | Ditolak | Ditolak | PASS |
| TC06 | Ketuntasan | Nilai 75, KKM 75 | Tuntas | Tuntas | PASS |
| TC07 | Data kosong | List kosong | Tidak terjadi pembagian nol | Mengembalikan None | PASS |
| TC08 | File tidak ditemukan | File tidak tersedia | Pesan kesalahan | FileNotFoundError ditangani | PASS |