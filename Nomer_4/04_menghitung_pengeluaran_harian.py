pengeluaranSebulan = []

for i in range(30):
    pengeluaranHarian = int(input(f"Masukan pengeluaran hari ke {i+1}: "))
    pengeluaranSebulan.append(pengeluaranHarian)

totalPengeluaran = 0
for i in range(pengeluaranSebulan.__len__()):
    totalPengeluaran += pengeluaranSebulan[i]

rata_rata_pengeluaran = totalPengeluaran / 30

print(totalPengeluaran)
print(rata_rata_pengeluaran)
