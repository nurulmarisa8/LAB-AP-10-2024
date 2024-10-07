def palindrome():
    input_string = input("Masukkan Palindrome: ")
    processed_string = input_string.replace(" ", "").lower()
    
    if processed_string == processed_string[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

palindrome()
