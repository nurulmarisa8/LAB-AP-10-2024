print("## Program Konversi Detik ##")

ssec = int(input("Masukkan Detik : ")) 
jam = ssec // 3600
sisadetik = ssec % 3600
menit = sisadetik // 60
detik = sisadetik % 60


print(f"{jam:02d}:{menit:02d}:{detik:02d}")