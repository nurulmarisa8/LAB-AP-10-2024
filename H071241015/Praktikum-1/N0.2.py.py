char = input('MASUKKAN KARAKTER: ')
sentence = input('MASUKKAN KALIMAT: ')

pesan = "Karakter merupakan bagian dari Kalimat" * (char in sentence) + "Karakter tidak ditemukan dalam Kalimat" * (char not in sentence)

print(pesan)