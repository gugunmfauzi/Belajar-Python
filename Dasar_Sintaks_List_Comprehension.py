print('\nPerintah del dengan list comperhension')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comperhension start')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
del daftar_buku[0:-1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comperhension start')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension')
daftar_buku = ['Seven Habits', 'Spatial Data', 'Data Science']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension ganjil')
daftar_buku = ['1 Seven Habits', '2 Spatial Data', '3 Data Science']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension genap')
daftar_buku = ['1 Seven Habits', '2 Spatial Data', '3 Data Science']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension dibuang diujung')
daftar_buku = ['1 Seven Habits', '2 Spatial Data', '3 Data Science']
daftar_buku_baru = daftar_buku[0:-2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension ganjil')
daftar_buku = ['1 Seven Habits', '2 Spatial Data', '3 Data Science']
print(daftar_buku[0::2])