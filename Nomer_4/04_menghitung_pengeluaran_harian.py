import locale

locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")

pengeluaranSebulan = []

for i in range(30):
    pengeluaranHarian = int(input(f"Masukan pengeluaran hari ke {i+1}: "))
    pengeluaranSebulan.append(pengeluaranHarian)

totalPengeluaran = 0
for i in range(pengeluaranSebulan.__len__()):
    totalPengeluaran += pengeluaranSebulan[i]

rata_rata_pengeluaran = totalPengeluaran / 30

print(
    f"\nTotal Pengeluaran Anda Sebesar: {locale.currency(totalPengeluaran, grouping=True)}")
print(
    f"Rata-Rata Pengeluaran Anda Sebesar: {locale.currency(rata_rata_pengeluaran, grouping=True)}\n")
