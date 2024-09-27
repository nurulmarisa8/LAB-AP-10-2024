def urutan(n):
    if n <= 0 or not isinstance(n, int):
        return "Input tidak Valid"
    
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        print(f"{n:.1f}")
    return f"Jumlah langkah: {steps}"

try:
    input_number = int(input("Masukan angka: "))
    result = urutan(input_number)
    print(result)
except ValueError:
    print("Input tidak Valid")
