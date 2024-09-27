def langkah(step):
    return step > 20

def harta_karun():
    total_jarak = 0
    bahaya = False

    while True:
        try:
            step = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if step < 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue
            if step == 0:
                break
            
            total_jarak += step
            
            if langkah(step):
                bahaya = True
                print("Ada bahaya: Ya")
                print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
        
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")


    print(f"Total jarak: {total_jarak} meter")
    if not bahaya:
        print("Ada bahaya: Tidak")
        if total_jarak == 50:
            print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
        else:
            print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
    else:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")

harta_karun()