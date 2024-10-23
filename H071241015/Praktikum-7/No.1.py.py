import os
from datetime import datetime

# Nama file untuk menyimpan data
FILM_FILE = "daftar_film.txt"
TIKET_FILE = "daftar_tiket.txt"

# ======== Fungsi Manajemen Film (Admin) ========
def tambah_film(judul, genre, durasi):
    with open(FILM_FILE, "a") as file:
        file.write(f"{judul},{genre},{durasi}\n")
    print(f"Film '{judul}' berhasil ditambahkan!")

def hapus_film(judul):
    if not os.path.exists(FILM_FILE):
        print("Tidak ada daftar film yang bisa dihapus.")
        return
    with open(FILM_FILE, "r") as file:
        films = file.readlines()
    with open(FILM_FILE, "w") as file:
        for film in films:
            if not film.startswith(judul):
                file.write(film)
    print(f"Film '{judul}' berhasil dihapus!")

def tampilkan_daftar_film():
    if not os.path.exists(FILM_FILE):
        print("Tidak ada film yang tersedia.")
        return
    with open(FILM_FILE, "r") as file:
        films = file.readlines()
        if films:
            print("Daftar Film:")
            for film in films:
                print(film.strip())
        else:
            print("Tidak ada film yang tersedia.")

# ======== Fungsi Pembelian Tiket (Pengunjung) ========
def beli_tiket(judul_film, nama_pengunjung):
    if not os.path.exists(FILM_FILE):
        print("Belum ada film yang tersedia untuk dibeli.")
        return

    # Generate ID tiket berdasarkan waktu
    id_tiket = generate_id_tiket()
    tanggal_beli = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Simpan informasi tiket ke dalam file
    with open(TIKET_FILE, "a") as file:
        file.write(f"{id_tiket},{judul_film},{nama_pengunjung},{tanggal_beli}\n")

    # Cetak tiket dalam format rapi
    cetak_tiket(id_tiket, judul_film, tanggal_beli)

def cetak_tiket(id_tiket, judul_film, tanggal):
    """Fungsi untuk mencetak tiket dalam format rapi."""
    tiket = f"""
+-------------------------------------+
|            TIKET BIOSKOP            |
+-------------------------------------+
| ID Tiket : {id_tiket:<20} |
| Film     : {judul_film:<20} |
| Tanggal  : {tanggal:<20} |
+-------------------------------------+
|     Terima kasih telah membeli      |
|             tiket Anda!             |
+-------------------------------------+
"""
    print(tiket)


# ======== Fungsi Manajemen Tiket (Admin) ========
def tampilkan_daftar_tiket():
    if not os.path.exists(TIKET_FILE):
        print("Belum ada tiket yang dibeli.")
        return
    with open(TIKET_FILE, "r") as file:
        tickets = file.readlines()
        if tickets:
            print("Daftar Tiket:")
            for ticket in tickets:
                print(ticket.strip())
        else:
            print("Belum ada tiket yang dibeli.")

def tampilkan_detail_tiket(id_tiket):
    if not os.path.exists(TIKET_FILE):
        print("Belum ada tiket yang tersedia.")
        return
    with open(TIKET_FILE, "r") as file:
        tickets = file.readlines()
        for ticket in tickets:
            if ticket.startswith(id_tiket):
                print(f"Detail Tiket: {ticket.strip()}")
                return
    print("Tiket tidak ditemukan.")

def hapus_tiket(id_tiket):
    if not os.path.exists(TIKET_FILE):
        print("Belum ada tiket yang bisa dihapus.")
        return
    with open(TIKET_FILE, "r") as file:
        tickets = file.readlines()
    with open(TIKET_FILE, "w") as file:
        for ticket in tickets:
            if not ticket.startswith(id_tiket):
                file.write(ticket)
    print(f"Tiket dengan ID '{id_tiket}' berhasil dihapus!")

# ======== Fungsi Tambahan ========
def generate_id_tiket():
    waktu_sekarang = datetime.now().strftime("%d%m%Y%H%M%S")
    return f"TICK{waktu_sekarang}"

def input_integer(prompt):
    """Menangani input berupa angka."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input tidak valid. Masukkan angka!")

# ======== Menu Utama ========
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Film")
        print("4. Tampilkan Daftar Tiket")
        print("5. Tampilkan Detail Tiket")
        print("6. Hapus Tiket")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Masukkan judul film: ")
            genre = input("Masukkan genre film: ")
            durasi = input_integer("Masukkan durasi film (menit): ")
            tambah_film(judul, genre, durasi)

        elif pilihan == "2":
            judul = input("Masukkan judul film yang ingin dihapus: ")
            hapus_film(judul)

        elif pilihan == "3":
            tampilkan_daftar_film()

        elif pilihan == "4":
            tampilkan_daftar_tiket()

        elif pilihan == "5":
            id_tiket = input("Masukkan ID tiket: ")
            tampilkan_detail_tiket(id_tiket)

        elif pilihan == "6":
            id_tiket = input("Masukkan ID tiket yang ingin dihapus: ")
            hapus_tiket(id_tiket)

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_pengunjung():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_daftar_film()

        elif pilihan == "2":
            judul_film = input("Masukkan judul film: ")
            nama_pengunjung = input("Masukkan nama pengunjung: ")
            beli_tiket(judul_film, nama_pengunjung)

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

def main():
    while True:
        print("\n=== Sistem Informasi Bioskop ===")
        print("1. Admin")
        print("2. Pengunjung")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengunjung()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()
