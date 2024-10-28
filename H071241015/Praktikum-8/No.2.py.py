import re

def cekip(n, input):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    hasil = []

    for ip in input:
        if re.fullmatch(ipv4_pattern, ip):
            hasil.append("IPv4")
        elif re.fullmatch(ipv6_pattern, ip):
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")
    
    return hasil

n = int(input("Masukkan jumlah baris: "))
input = [input(f"Masukkan IP ke-{i + 1}: ") for i in range(n)]

hasil = cekip(n, input)
for r in hasil:
    print(r)



