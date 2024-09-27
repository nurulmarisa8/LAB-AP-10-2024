def kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")

    try:

        angka_pertama = int(input("Angka pertama: "))
        angka_kedua = int(input("Angka kedua: "))
        operasi = input("Operasi (+, -, *, /): ")

        if operasi == '+':
            hasil = angka_pertama + angka_kedua
        elif operasi == '-':
            hasil = angka_pertama - angka_kedua 
        elif operasi == '*':
            hasil = angka_pertama * angka_kedua
        elif operasi == '/':
            if angka_kedua != 0:
                hasil = angka_pertama / angka_kedua
            else:
                return "Pembagian dengan nol tidak diperbolehkan."
        else:
            return "Operasi tidak valid. Gunakan +, -, *, atau /."
        
        return f"Hasil: {hasil}"
    
    except ValueError as e:
        return f"Input tidak valid: could not convert string to float: {e}"

print(kalkulator_sederhana())