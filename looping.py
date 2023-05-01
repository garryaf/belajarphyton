# menginisialisasi variabel sebelumnya sebagai None
sebelumnya = None

# melakukan looping tak terbatas
while True:
    # meminta pengguna memasukkan angka
    angka = input("Masukkan angka: ")

    # memeriksa apakah angka yang dimasukkan sama dengan sebelumnya
    if angka == sebelumnya:
        print("Anda memasukkan angka yang sama. Silakan coba lagi.")
        continue

    # jika angka yang dimasukkan berbeda, mencetak angka dan memperbarui nilai sebelumnya
    print("Anda memasukkan angka:", angka)
    sebelumnya = angka