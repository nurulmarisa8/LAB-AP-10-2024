ketupat = int(input('Masukkan Jumlah Baris: '))
print()

for i in range(ketupat):
    if i % 2 == 1:
        continue
    else:
        print(' ' * (ketupat - i) + '* ' * (i + 1))

if ketupat % 2 == 1:
    for i in range(ketupat):
        if i % 2 == 0:
            continue
        else:
            print(' ' * (i + 2) + '* ' * (ketupat - i - 1))
else:
    for i in range(ketupat):
        if i % 2 == 0:
            continue
        else:
            print(' ' * (i + 1) + '* ' * (ketupat - i))