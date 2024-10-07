def anagram(str1, str2):
    freq1 = {}
    freq2 = {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1
    
    hapus = 0 # menyimpan jumlah karakter yg di hapus
    
    for char in freq1:
        if char in freq2:
            hapus += abs(freq1[char] - freq2[char])
        else:
            hapus += freq1[char]

    for char in freq2:
        if char not in freq1:
            hapus += freq2[char]
    
    return hapus

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

print("Jumlah minimum penghapusan untuk membuat anagram:", anagram(str1, str2))