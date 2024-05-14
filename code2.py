a = [[1,2,3],[2,3,4],[3,4,5]]
b = []
v = 0
for i in a:
    for j in i:
        j += j
    print(j)