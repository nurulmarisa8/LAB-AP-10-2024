# INPUT WAHANA
U = int(input("MASUKKAN UMUR: "))

# SISTEM 
if U < 5:
    Bayar = 0
elif 5 <= U <= 12:
    Bayar = 50000
elif 13 <= U <= 59:
    Bayar = 100000
else:
    Bayar = 70000

anggota = input("APAKAH MEMILIKI KARTU ANGGOTA (YA/TIDAK): ")

diskon = Bayar - (Bayar * 20/100)

hargatiket = diskon if anggota == "YA" else Bayar

print(f'Harga Tiket: Rp.{hargatiket:.0f}')