# Meminta pengguna memasukkan angka n
n = int(input("Masukkan angka n:"))
# Melakukan perulangan dari angka 1 hingga n
for i in range(1, n+1):
    # Mengecek apakah i adalah angka ganjil (tidak bisa dibagi 2)
    if i % 2 != 0:
        # Jika i ganjil, cetak i
        print(i)

# Setelah perulangan selesai, program berhenti
