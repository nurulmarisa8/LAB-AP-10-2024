pa = int(input("Masukkan populasi awal Serangga A: "))
pb = int(input("Masukkan populasi awal Serangga B: "))

N = int(input("Masukkan jumlah hari: "))

for hari in range(1, N+1):
    if hari % 2 == 1: 
        pa =int(pa * 1.3) 
        pb =int(pb * 1.5) 
    else:
        pa =int(pa * 0.8)
        pb =int(pb * 0.6)
        
    if hari % 5 == 0:
        pa =int(pa * 0.9)  
        pb =int(pb * 0.9) 
        print(f"Hari {hari}: Predator memakan 10% populasi")
    else:
        print(f"Hari {hari}: Serangga A = {pa:.0f}, Serangga B = {pb:.0f}")