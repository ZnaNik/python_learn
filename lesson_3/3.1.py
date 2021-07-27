dict = {2: 0, 9:0}
nat_array = [el for el in range(2,100)]

for i in nat_array:
    if (i % 9 == 0):
        dict[9] = dict[9]+1
    if (i % 2 == 0):
        dict[2] = dict[2] + 1

print(dict)


