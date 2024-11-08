import os

print("Welcome to Ftp Tools b3st0fyou")
print("Pilih Lah:")
print("1. Ftp Grab")
print("2. Ftp Split")
print("3. Ftp Cek")
print("4. Dorkers")

def screen_clear():
    os.system('cls')
# Input pilihan pengguna
pilihan = input("Masukan Pilihan Angka 1, 2, 3 atau 4: ")

# Cek input pengguna dan jalankan file yang sesuai
if pilihan == "1":
    os.system("python script/ftprun.py")
elif pilihan == "2":
    os.system("python script/ftpsplit.py")
elif pilihan == "3":
    os.system("python script/ftpcheck.py")
elif pilihan == "4":
    os.system("python script/searcherv3.py")
else:
    print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3 atau 4.")
