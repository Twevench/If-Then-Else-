# Meminta input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Menggunakan if, elif, dan else untuk menentukan kategori usia
if usia < 12:
    print("Anda adalah anak-anak.")
elif 12 <= usia < 18:
    print("Anda adalah remaja.")
elif 18 <= usia < 60:
    print("Anda adalah dewasa.")
else:
    print("Anda adalah lansia.")
