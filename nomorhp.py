import phonenumbers
from phonenumbers import geocoder

# Masukkan nomor handphone Anda dengan format internasional
nomor_hp = "+6281321559215"

# Parse nomor handphone menggunakan library phonenumbers
nomor_hp_parsed = phonenumbers.parse(nomor_hp)

# Mendapatkan informasi tentang lokasi nomor handphone
lokasi = geocoder.description_for_number(nomor_hp_parsed, "id")

# Cetak hasil
print("Nomor handphone", nomor_hp, "berlokasi di", lokasi)