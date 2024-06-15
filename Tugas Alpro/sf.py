def a(a, b):
    return a % b

result = 0
for i in range(1, 11):
    if a(i, 2) == 0:
        result = result + i
    else :
        result = result - i
print(result)
