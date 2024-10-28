import re

# Input dari pengguna
input_string = input("Masukkan string (45 karakter): ")

# Memastikan panjang string tepat 45 karakter
if len(input_string) != 45:
    print(False)
else:
    # 40 karakter pertama
    karakter40awal = input_string[:40]
    if not re.match(r'^[A-z0-9]{40}$', karakter40awal):
        print(False)
    else:
        # 5 karakter terakhir
        karakter5terakhir = input_string[40:]
        if not re.match(r'^[13579\s]{5}$', karakter5terakhir):
            print(False)
        else:
            print(True)