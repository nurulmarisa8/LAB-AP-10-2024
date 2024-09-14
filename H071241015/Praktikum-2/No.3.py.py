# INPUT
Nilai = int(input("MASUKKAN NILAI MAHASISWA: "))
Absen = int(input("MASUKKAN PRESENTASI ABSEN: "))

# PROGRAM SISTEM NILAI
if Absen >= 75:
    if 85 <= Nilai <= 100:
        print("Lulus dengan Predikat A")
    elif 70 <= Nilai <= 84:
        print("Lulus dengan Predikat B")
    elif 60 <= Nilai <= 69:
        print("Lulus dengan Predikat C")
    elif Nilai < 60:
        tambahtugas = int(input("MASUKKAN NILAI TAMBAH TUGAS: "))
        if tambahtugas > 70:
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
else:
    print("Tidak Lulus")