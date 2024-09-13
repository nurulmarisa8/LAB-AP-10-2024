print("Program Konversi Suhu")

celcius = float(input("Masukkan Suhu Celcius : "))

kelvin = celcius + 273.15
reamur = celcius * (4/5)
fahrenheit = (9/5 * celcius) + 32

print(celcius, "Derajat Celcius =", kelvin, "Derajat Kelvin")
print(celcius, "Derajat Celcius =", reamur, "Derajat Reamur")
print(celcius, "Derajat Celcius =", fahrenheit, "Derajat Fahrenheit")