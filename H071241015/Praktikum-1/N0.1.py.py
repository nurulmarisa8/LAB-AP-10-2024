s = float(input('MASUKKAN HARGA SAHAM YANG AKAN DI BELI: '))

saham_now = 105.0
perubahan = ((saham_now - s)/s) * 100

Beli = (perubahan > 5) * 1
Tahan = (perubahan <= 5) * (perubahan >= -3) * 1 
Jual = (perubahan <= -3) * 1

allin = Beli * 'Beli' + Tahan * 'Tahan' + Jual * 'Jual'

print(f"Perubahan Presentasi Saham: {perubahan:.2f}%")
print(f"Rekomendasi Invest: {allin}")
 