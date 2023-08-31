try:
    bilangan = int(input("Masukkan Suatu Angka: "))

    if bilangan > 0:
        print("Bilangan Positif")
    elif bilangan == 0:
        print("Bilangan Nol!")
    elif bilangan < 0:
        print("Bilangan Negatif!")
except ValueError:
    print("Mohon masukkan angka yang valid!")
