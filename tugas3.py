# Meminta pengguna untuk memasukkan sebuah angka (n)
n = int(input("Masukkan Angka: "))

# Inisialisasi dua nilai pertama dari deret Fibonacci: a = 0 dan b = 1
a, b = 0, 1

# Mencetak judul untuk output deret Fibonacci
print("Bilangan Fibonaccinya adalah : ")

# Perulangan untuk menampilkan deret Fibonacci sebanyak n kali
for i in range(n):
   # Jika nilai a kurang dari atau sama dengan 10, cetak nilai a
    if a <= 10:
        print(a, end=" ")  # Mencetak nilai a di baris yang sama, dipisahkan oleh spasi

    # Memperbarui nilai a dan b, di mana a menjadi b, dan b menjadi jumlah a + b
    a, b = b, a + b

# Mencetak baris baru setelah loop selesai
print()
