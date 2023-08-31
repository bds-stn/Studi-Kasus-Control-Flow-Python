namaSiswa = input("Masukkan nama anda: ")
print()
nilaiMTK = int(input("Masukkan nilai MTK anda: "))
nilaiIPA = int(input("Masukkan nilai IPA anda: "))
nilaiIPS = int(input("Masukkan nilai IPS anda: "))
nilaiBjawa = int(input("Masukkan nilai B. Jawa anda: "))
nilaiBindo = int(input("Masukkan nilai B. Indo anda: "))

rata_rata = (nilaiMTK + nilaiIPA + nilaiIPS + nilaiBjawa + nilaiBindo) / 5

grade = ""

if rata_rata >= 90 and rata_rata <= 100:
    grade = "A"
elif rata_rata >= 80 and rata_rata <= 89:
    grade = "B"
elif rata_rata >= 70 and rata_rata <= 79:
    grade = "C"
elif rata_rata >= 60 and rata_rata <= 69:
    grade = "D"
elif rata_rata < 60:
    grade = "E"

if grade == "A" or grade == "B" or grade == "C":
    print(
        f"\nSelamat {namaSiswa}, Rata-Rata Anda {rata_rata} dan Anda Dinyatakan Lulus Dengan Grade {grade}!")
else:
    print(
        f"\nMohon maaf {namaSiswa}, Anda Mendapatkan Grade {grade} Dengan Rata-Rata {rata_rata} Sehingga Anda Dinyatakan Tidak Lulus!")
