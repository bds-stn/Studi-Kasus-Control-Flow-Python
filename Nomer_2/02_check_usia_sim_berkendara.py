usia = int(input("Masukkan Usia Anda: "))
punyaSim = input("Apakah Anda Memiliki SIM? (y/t) ")

if (usia > 17 and punyaSim == "y"):
    print("Anda layak mengendarai mobil")
elif (usia <= 17 or punyaSim == "t"):
    print("Anda tidak layak mengendarai mobil")
