"""
Program pengulangan membaca buku undefined count
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua buku"')
buku = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while buku < jumlah_buku * 2:
    buku = buku + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} belum paham")
    else :
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else :
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')

