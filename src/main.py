import math
from pathlib import Path

from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik
from utilitas import tentukan_status
kkm = float(input("Masukkan nilai KKM (default 75): ") or 75)

if not math.isfinite(kkm) or kkm < 0 or kkm > 100:
    print("KKM harus berupa angka antara 0 sampai 100.")
