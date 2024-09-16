# PAKET A
import math

sisi1 = int(input("PANJANG SISI X: "))
sisi2 = int(input("PANJANG SISI Y: "))

luas = 1/2 * (sisi2 * sisi1)
sisim = math.sqrt(sisi1**2 + sisi2**2)
keliling = sisi1 + sisi2 + sisim

print(f'Luas Permukaan: {luas:.2f}')
print(f'Keliling: {keliling:.2f}')