import random
angka_rahasia = random.randint(1, 100)

percobaan = 5

print("Tebak angka antara 1 sampai 100.")

for i in range(percobaan):
    tebakan = int(input(f"Tebakan ke-{i+1}: "))
    if tebakan == 0:
        print("Permainan dihentikan.")
        break
    elif tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
if tebakan != angka_rahasia:
    print(f"Sayang sekali, angka yang benar adalah {angka_rahasia}.")