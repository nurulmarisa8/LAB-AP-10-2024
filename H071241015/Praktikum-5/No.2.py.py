def singkat_kata_depan():
    input = input("Masukkan kalimat: ")
    kata_kata = input.split()

    singkatan = ''.join([kata[0] for kata in kata_kata])
    
    print(singkatan)

singkat_kata_depan()
