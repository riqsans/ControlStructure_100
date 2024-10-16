# Meminta pengguna memasukkan nilai n
n = int(input("Masukkan nilai n:"))

# Melakukan perulangan dari angka 1 hingga n
for i in range(1, n+1):
    # looping sebanyak i kali untuk mencetak angka i
    for j in range(i):
        # Mencetak angka i dalam satu baris, dipisahkan oleh spasi
        print(i, end=" ")
    # Setelah mencetak satu baris, pindah ke baris baru
    print()
