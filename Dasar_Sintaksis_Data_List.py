daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
print('tampilkan variabel daftar buku')
print(daftar_buku)

print('Proses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('Tampilkan isi daftarbuku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 2.14]
print('\nTampilkan dengan in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
daftar_buku[0] = 'Atomic Habit'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -2')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
