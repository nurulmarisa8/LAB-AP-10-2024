# Fungsi untuk menghitung total nilai stok
def hitung_total_stok(jumlah, harga):
    return jumlah * harga

# Fungsi untuk memberikan rekomendasi berdasarkan nilai stok
def rekomendasi_nilai_stok(total_stok):
    if total_stok > 1000000:
        return "Nilai stok tinggi, pastikan penjualan berjalan lancar."
    elif 500000 <= total_stok <= 1000000:
        return "Nilai stok sedang, periksa stok dengan cermat."
    else:
        return "Nilai stok rendah, pertimbangkan menambah stok."

# Fungsi untuk memperbarui file jika ada data dengan nama barang yang sama
def update_file(nama_barang, jumlah, harga, total_stok):
    try:
        with open("inventaris.txt", "r") as file:
            lines = file.readlines()
        
        # Cek apakah nama barang sudah ada, jika ya perbarui datanya
        data_baru = []
        barang_ditemukan = False
        for line in lines:
            if line.startswith(f"Nama Barang: {nama_barang},"):
                data_baru.append(f"Nama Barang: {nama_barang}, Jumlah Stok: {jumlah}, Harga per Unit: {harga}, Total Nilai Stok: {total_stok}\n")
                barang_ditemukan = True
            else:
                data_baru.append(line)
        
        # Jika nama barang tidak ditemukan, tambahkan data baru
        if not barang_ditemukan:
            data_baru.append(f"Nama Barang: {nama_barang}, Jumlah Stok: {jumlah}, Harga per Unit: {harga}, Total Nilai Stok: {total_stok}\n")
        
        # Tulis ulang file dengan data baru
        with open("inventaris.txt", "w") as file:
            file.writelines(data_baru)
        return barang_ditemukan
    except FileNotFoundError:
        # Jika file belum ada, buat file baru dan tambahkan data
        with open("inventaris.txt", "w") as file:
            file.write(f"Nama Barang: {nama_barang}, Jumlah Stok: {jumlah}, Harga per Unit: {harga}, Total Nilai Stok: {total_stok}\n")
        return False

# Fungsi untuk membaca data dari file
def baca_file():
    try:
        with open("inventaris.txt", "r") as file:
            data = file.read()
            return data if data else "Data inventaris kosong."
    except FileNotFoundError:
        return "File inventaris belum ada."

# Kelas untuk barang
class Barang:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def hitung_total_stok(self):
        return self.jumlah * self.harga

    def rekomendasi(self):
        total_stok = self.hitung_total_stok()
        return rekomendasi_nilai_stok(total_stok)

# Main program
while True:
    print("\n=== Manajemen Inventaris Toko ===")
    print("1. Tambah atau perbarui data barang")
    print("2. Lihat data barang")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == "1":
        # Input data barang
        nama_barang = input("Masukkan nama barang: ").strip()
        if not nama_barang:
            print("Nama barang tidak boleh kosong!")
            continue

        try:
            jumlah_stok = int(input("Masukkan jumlah stok: "))
            harga_per_unit = int(input("Masukkan harga per unit: "))

            if jumlah_stok < 0 or harga_per_unit < 0:
                print("Jumlah stok dan harga harus angka positif!")
            else:
                # Menggunakan fungsi untuk menghitung dan memberikan rekomendasi
                total_nilai_stok = hitung_total_stok(jumlah_stok, harga_per_unit)
                print(f"Total nilai stok: {total_nilai_stok}")
                print(rekomendasi_nilai_stok(total_nilai_stok))

                # Simpan atau perbarui data di file
                barang_ditemukan = update_file(nama_barang, jumlah_stok, harga_per_unit, total_nilai_stok)
                if barang_ditemukan:
                    print("Data barang berhasil diperbarui!")
                else:
                    print("Data barang berhasil ditambahkan!")

                # Menggunakan OOP untuk menampilkan informasi (opsional)
                barang = Barang(nama_barang, jumlah_stok, harga_per_unit)
                print("\n=== Menggunakan OOP ===")
                print(f"Total nilai stok: {barang.hitung_total_stok()}")
                print(barang.rekomendasi())
        except ValueError:
            print("Input harus berupa angka yang valid!")

    elif pilihan == "2":
        # Membaca data dari file
        print("\n=== Data Inventaris ===")
        print(baca_file())

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
