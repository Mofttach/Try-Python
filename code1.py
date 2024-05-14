var_input = [1,2,3,4,5,6]
var_output = []

for i in var_input:
    if i % 2 == 0:
        var_output.append('genap')
    else:
        var_output.append('ganjil')

print(var_output)