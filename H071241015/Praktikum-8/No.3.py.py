import re
user = input("Masukkan Username : ")
email = input("Masukkan Email : ")
password = input("Password Email : ")

def valid_username(user):
    pattern = r'^[a-zA-Z0-9*\d]{1}[a-zA-Z0-9*\d]{5,20}$'
    if re.fullmatch(pattern, user):
        return "Username Valid"
    else:
        return "Username Tidak Valid"

def valid_email(email):
    pattern = r'^[a-z0-9]+[0-9]*@[a-z]+\.[a-z]{2,3}(\.[a-z]{2,3})?$'

    if re.fullmatch(pattern, email):
        return "Email valid"
    else:
        return "Email yang kamu input tidak valid. Registrasi gagal!"

def valid_password(password):
    pattern = r'^[a-zA-Z0-9*\d]{1}[a-zA-Z0-9*\d]{8, }$'

    if re.fullmatch(pattern, password):
        return "Password valid"
    else:
        return "Password tidak valid"

print(valid_username(user))
print(valid_password(password))
print(valid_email(email))