"""
ini adalah percobaaan pertama
Pada tahap ini saya akan belaja mengenai semua sintaksis darasr bahasa pemrograman terdiri dari :
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

#1. Sekuensial
print("Hello world")
print("My name is Gugun")
print(1)
print(2*3)
print('Ibu menjawab, "Baik,apa yang harus saya lakukan?"')
print("Saya Membawa Laptop")

#2. Pecabangan
jumlah_botol_susu = 160
jumlah_telor = 1996
print(f"Jumlah botol susu {jumlah_botol_susu} btl")
print(f"Jumlah telor {jumlah_telor} btr")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telor == 0:
        print("Budi membeli 1 botol susu")
    else :
        print("Budi membeli 6 botol susu")
else :
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya ke ibu")