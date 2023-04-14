input_valid = False

while not input_valid:
    angka = input("Masukkan angka (tidak boleh lebih dari 6 digit dan tidak boleh menggunakan angka 1): ")
    if len(angka) > 6:
        print("Angka terlalu panjang!")
    elif '1' in angka:
        print("Angka 1 tidak diizinkan!")
    else:
        try:
            angka = int(angka)
            if angka > 999999:
                print("Angka terlalu besar!")
            else:
                input_valid = True
        except ValueError:
            print("Input harus berupa angka!")

total = sum(int(digit) for digit in str(angka))

if total == 8:
    print("Hasil adalah 8")
else:
    print("Hasil bukan 8, hasil adalah", total)