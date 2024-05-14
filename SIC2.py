list_input = [800, 600, 400, 200]
commpared_input = [500, 200, 400]

for i in range(len(list_input)):
    if list_input[i] in commpared_input:
        list_input[i] = 1
    else:
        list_input[i] = 0
    print(list_input)
    