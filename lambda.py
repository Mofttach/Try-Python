add = lambda x, y : x + y
print(add(2,3))

print('-----------pemisah---------')

umur = [19, 18, 20, 65, 21, 45, 35, 63]
print('Umur diatas 21 tahun adalah :')

for i in filter(lambda x: x >= 21, umur):
    print(i, end = " ")

print('-----------pemisah---------')
# Map

a = [1,2,3,4,5,6]

kuadrat = list(map(lambda x: x**2, a))
print(kuadrat)

# Lamda Reduce
from functools import reduce

n = reduce(lambda x, y : x+y , a)
print(n)

a = [1,2,3]
n = reduce(lambda x,y : x + (x*y), a)
print(n)