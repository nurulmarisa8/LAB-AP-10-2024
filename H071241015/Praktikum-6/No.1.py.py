# INVENTORY
inventory = []  

def tampilkan_menu():
    """MAIN MENU"""
    print("\n=== MENU INVENTORY BARANG ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def tambah_barang():
    """ADD ITEM TO INVENTORY"""
    kode = input("Masukkan kode barang: ")  
    nama = input("Masukkan nama barang: ")  
    jumlah = int(input("Masukkan jumlah barang: "))  
    harga = float(input("Masukkan harga barang: "))  

    # Tambahkan barang ke dalam inventory
    barang = {
        "kode": kode,
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga
    }
    inventory.append(barang)  
    print(f"Barang '{nama}' dengan kode '{kode}' berhasil ditambahkan.")

def hapus_barang():
    """REMOVE ITEM BY KODE"""
    kode = input("Masukkan kode barang yang akan dihapus: ")  
    for barang in inventory:
        if barang["kode"].lower() == kode.lower():
            inventory.remove(barang)
            print(f"Barang dengan kode '{kode}' berhasil dihapus.")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")

def tampilkan_daftar_barang():
    """VIEW ALL INVENTORY ITEMS"""
    if not inventory:
        print("Tidak ada barang dalam inventory.")
    else:
        print("\n=== DAFTAR BARANG ===")
        nomor = 1
        for barang in inventory:
            print(f"{nomor}. Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: Rp {barang['harga']}")
            nomor += 1

def cari_barang():
    """SEARCH ITEM BY KODE OR NOMOR"""
    pilihan = input("Cari berdasarkan (1) Nomor atau (2) Kode? Masukkan pilihan: ")

    if pilihan == "1":  # Cari berdasarkan kode barang
            kode = input("Masukkan kode barang: ")  
            for barang in inventory:
                if barang["kode"].lower() == kode.lower():
                    print(f"Barang ditemukan: Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: Rp {barang['harga']}")
                    return
            print(f"Barang dengan kode '{kode}' tidak ditemukan.")

    elif pilihan == "2":  # Cari berdasarkan kode barang
        nama = input("Masukkan Nama barang: ")  
        for barang in inventory:
            if barang["nama"].lower() == nama.lower():
                print(f"Barang ditemukan: Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: Rp {barang['harga']}")
                return
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def update_barang():
    """UPDATE ITEM BY KODE"""
    kode = input("Masukkan kode barang yang akan diupdate: ")  
    for barang in inventory:
        if barang["kode"].lower() == kode.lower():
            print("Data ditemukan. Masukkan data baru.")
            barang["nama"] = input("Masukkan nama baru: ")  
            barang["jumlah"] = int(input("Masukkan jumlah baru: "))  
            barang["harga"] = float(input("Masukkan harga baru: "))  
            print(f"Data barang dengan kode '{kode}' berhasil diperbarui.")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")

def main():
    """MAIN PROGRAM"""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")  

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_daftar_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

main()
