import sys
import unittest
import tempfile

from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from utilitas import validasi_nilai, tentukan_status
from analisis import hitung_statistik
from data_io import baca_data


class TestProgram(unittest.TestCase):

    def test_nilai_normal(self):
        valid, nilai, pesan = validasi_nilai("80")
        self.assertTrue(valid)
        self.assertEqual(nilai, 80)

    def test_nilai_batas_bawah(self):
        valid, nilai, pesan = validasi_nilai("0")
        self.assertTrue(valid)
        self.assertEqual(nilai, 0)

    def test_nilai_batas_atas(self):
        valid, nilai, pesan = validasi_nilai("100")
        self.assertTrue(valid)
        self.assertEqual(nilai, 100)

    def test_nilai_melebihi_batas(self):
        valid, nilai, pesan = validasi_nilai("105")
        self.assertFalse(valid)

    def test_nilai_bukan_angka(self):
        valid, nilai, pesan = validasi_nilai("abc")
        self.assertFalse(valid)

    def test_nilai_nan(self):
        valid, nilai, pesan = validasi_nilai("nan")
        self.assertFalse(valid)

    def test_status_tuntas(self):
        status = tentukan_status(75, 75)
        self.assertEqual(status, "Tuntas")

    def test_status_belum_tuntas(self):
        status = tentukan_status(60, 75)
        self.assertEqual(status, "Belum Tuntas")

    def test_hitung_statistik(self):
        data = [
            {"nama": "Andi", "nilai": 80},
            {"nama": "Budi", "nilai": 70},
            {"nama": "Citra", "nilai": 90}
        ]

        hasil = hitung_statistik(data)

        self.assertEqual(hasil["jumlah_siswa"], 3)
        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["nilai_tertinggi"], 90)
        self.assertEqual(hasil["nilai_terendah"], 70)

    def test_data_kosong(self):
        hasil = hitung_statistik([])
        self.assertIsNone(hasil)

    def test_baca_data(self):
        with tempfile.TemporaryDirectory() as folder:
            file_data = Path(folder) / "nilai.txt"

            file_data.write_text(
                "Andi,80\nBudi,70\nCitra,90",
                encoding="utf-8"
            )

            data, kesalahan = baca_data(file_data)

            self.assertEqual(len(data), 3)
            self.assertEqual(len(kesalahan), 0)

    def test_data_tidak_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            file_data = Path(folder) / "nilai.txt"

            file_data.write_text(
                "Andi,80\nBudi,abc\nCitra,90",
                encoding="utf-8"
            )

            data, kesalahan = baca_data(file_data)

            self.assertEqual(len(data), 2)
            self.assertEqual(len(kesalahan), 1)

    def test_file_tidak_ditemukan(self):
        with self.assertRaises(FileNotFoundError):
            baca_data("file_tidak_ada.txt")


if __name__ == "__main__":
    unittest.main()