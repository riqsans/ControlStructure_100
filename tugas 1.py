# Meminta pengguna memasukkan nilai persentase
percentage = float(input("Masukkan presentasenya: "))

# Mengecek apakah persentase lebih besar atau sama dengan 90, jika ya, cetak "Excellent"
if percentage >= 90:
    print("Excellent")
# Jika persentase lebih besar atau sama dengan 80 tetapi kurang dari 90, cetak "Very good"
elif percentage >= 80:
    print("Very good")
# Jika persentase lebih besar atau sama dengan 70 tetapi kurang dari 80, cetak "Good"
elif percentage >= 70:
    print("Good")
# Jika persentase lebih besar atau sama dengan 60 tetapi kurang dari 70, cetak "Average"
elif percentage >= 60:
    print("Average")
# Jika persentase kurang dari 60, cetak "Needs improvement"
else:
    print ("Needs improvement")
