angka = [i for i in range(0,999)]
for i in angka:
    if i % 5 == 3:
        if i % 7 == 5:
            if i % 11 == 7 :
                print(i)


hasil = 733
print(hasil % 5)
print(hasil % 7)
print(hasil % 11)