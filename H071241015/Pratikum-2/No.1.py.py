# INPUT
sisi1 = int(input("Masukkan Jumlah Sisi 1: "))
sisi2 = int(input("Masukkan Jumlah Sisi 2: "))
sisi3 = int(input("Masukkan Jumlah Sisi 3: "))

# PROGRAM SEGITIGA
if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
    print("Sisi harus memiliki panjang lebih dari nol")
elif sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1:
    print("Tidak dapat membentuk segitiga yang valid")
elif sisi1 == sisi2 == sisi3:
    print("Segitiga Sama Sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")

