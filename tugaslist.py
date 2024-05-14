#Buat List bernama hewan berisi ayam, sapi, dan kambing
hewan = ['ayam', 'sapi', 'kambing']
print(hewan)

#Ganti hewan sapi menjadi katak
hewan[1] = 'katak'
print(hewan)

#Hapus hewan no 2 dari belakang
del hewan[-2]
print(hewan)
#Tambahkan Gajah dibagian paling depan
hewan.insert(0, 'Gajah')

#Buat list baru bernama hewan2 berisi ikan
hewan2 = ['ikan']
#Gabungkan kedua list
hewan3 = hewan + hewan2
print(hewan3)
#print hasil disetiap step nya 😎

tup1 = ('Syahroni', 'faiq', 'irf4n')
tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tup3 = (tup1, tup2)
print(tup3)
#Cara mengakses data 3 (angka3) di tup3

a = tup3[1][2]
print(a)
