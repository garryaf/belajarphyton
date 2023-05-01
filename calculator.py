# definisikan fungsi untuk setiap operasi
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

# menampilkan menu pilihan operasi
print("Pilih operasi.")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# meminta pengguna memilih operasi
pilihan = input("Masukkan pilihan(1/2/3/4): ")

# meminta pengguna memasukkan dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# melakukan operasi yang dipilih
if pilihan == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
elif pilihan == '2':
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
elif pilihan == '3':
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
elif pilihan == '4':
    print(angka1, "/", angka2, "=", bagi(angka1, angka2))
else:
    print("Input yang dimasukkan salah")