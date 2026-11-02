def hitung_statistik(daftar_siswa):
    """
    Menghitung jumlah siswa, total nilai,
    rata-rata, nilai tertinggi, dan nilai terendah.
    """

    if not daftar_siswa:
        return None

    daftar_nilai = [
        siswa["nilai"] for siswa in daftar_siswa
    ]

    jumlah_siswa = len(daftar_nilai)
    total_nilai = sum(daftar_nilai)
    rata_rata = total_nilai / jumlah_siswa

    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    return {
        "jumlah_siswa": jumlah_siswa,
        "total_nilai": total_nilai,
        "rata_rata": rata_rata,
        "nilai_tertinggi": nilai_tertinggi,
        "nilai_terendah": nilai_terendah
    }