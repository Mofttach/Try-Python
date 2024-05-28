
n = int(input("Berapa banyak nya Bilangan : "))
total = 0
   
bil_terbesar = None
bil_terkecil = None

for i in range(1, n + 1):
    bil = int(input(f'Bilangan ke {i} : '))
    total = total + bil
    if bil_terbesar is None or bil > bil_terbesar:
        bil_terbesar = bil
    if bil_terkecil is None or bil < bil_terkecil:
        bil_terkecil = bil

print(f'Totalnya adalah {total}')
print(f'Bilangan terbesar adalah {bil_terbesar}')
print(f'Bilangan terkecil adalah {bil_terkecil}')





