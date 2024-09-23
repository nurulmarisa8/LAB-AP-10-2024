total = int(input("Masukkan total harga: "))
bayar = int(input("Masukkan uang yang dibayar: "))

kembalian = bayar - total

if kembalian < 0:
  print("Uang yang diberikan kurang.")
else:
  print("Kembalian:", kembalian)
  uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
  for uang in uang:
    jumlah = kembalian // uang
    kembalian %= uang
    if jumlah > 0:
      print(f"{jumlah} lembar {uang}")