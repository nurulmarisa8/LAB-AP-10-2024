def caesar_cipher(text, shift):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    result = ''
    
    for char in text:
        if char in lower_alphabet:
            result += lower_alphabet[(lower_alphabet.index(char) + shift) % 26]
        elif char in upper_alphabet:
            result += upper_alphabet[(upper_alphabet.index(char) + shift) % 26]
        else:
            result += char  # Keep numbers and special characters unchanged
    
    return result

# Input
text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

# Output
print("Cipher:", caesar_cipher(text, shift))
