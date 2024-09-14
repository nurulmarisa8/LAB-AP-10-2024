# INPUT
data = int(input("Masukkan jumlah data yang Anda gunakan: "))
penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (tidak-sibuk) atau di jam sibuk (sibuk)? ")
pilihan = input("Apakah Anda pengguna Personal atau Bisnis? ")

# PROGRAM DATA
if data < 10 and penggunaan == "tidak-sibuk" and pilihan == "personal":
    print("Paket yang Sesuai: Paket A")
elif 10 <= data <= 50 and penggunaan == "sibuk" and pilihan == "personal":
    print("Paket yang Sesuai: Paket B")
elif data > 50 and penggunaan == "sibuk" and pilihan == "personal" == "bisnis":
    print("Paket yang Sesuai: Paket C")
elif data > 50 and penggunaan == "tidak-sibuk" and pilihan == "bisnis":
    print("Paket yang Sesuai: Paket D")
else:
    print("Tidak Ada Paket yang Cocok")