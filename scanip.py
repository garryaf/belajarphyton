import socket

# Meminta input dari pengguna untuk alamat IP
subnet = input("Masukkan alamat IP subnet (format xxx.xxx.xxx.): ")
start = int(input("Masukkan nomor IP awal: "))
end = int(input("Masukkan nomor IP akhir: "))

# Looping untuk mengiterasi alamat IP
for i in range(start, end+1):
    ip = subnet + str(i)
    try:
        # Mencoba membuat koneksi dengan alamat IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, 80))
        if result == 0:
            print(ip, "is up and running")
        s.close()
    except:
        pass