N = int(input("Masukkan Nilai N: "))  
M = int(input("Masukkan Nilai M: ")) 

move_kanan = True

for i in range(N):
    if move_kanan:
        for j in range(M):
            print(f"MOVE ({i},{j})")
    else:
        for j in range(M-1, -1, -1):
            print(f"MOVE ({i},{j})")

    move_kanan = not move_kanan
