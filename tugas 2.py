# Meminta pengguna memasukkan angka pertama dan mengonversinya menjadi tipe float
num1 = float(input("Masukkan Angka Pertama:"))

# Meminta pengguna memasukkan angka kedua dan mengonversinya menjadi tipe float
num2 = float(input("Masukkan Angka Kedua:"))

# Meminta pengguna memasukkan angka ketiga dan mengonversinya menjadi tipe float
num3 = float(input("Masukkan Angka Ketiga: "))

# Memeriksa apakah num1 adalah angka terbesar dibandingkan num2 dan num3
if num1 >= num2 and num1 >= num3:
    largest = num1
# Jika kondisi pertama salah, memeriksa apakah num2 adalah yang terbesar
elif num2 >= num1 and num2 >= num3:
    largest = num2
# Jika kedua kondisi di atas salah, maka num3 adalah angka terbesar
else:
    largest = num3

# Mencetak angka terbesar yang telah ditemukan
print (f"Angka Terbesar adalah: {largest}")
