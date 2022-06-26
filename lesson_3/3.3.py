#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

#Генерируем массив случайных числе
arr = [random.randint(-50,50) for el in range(0,50)]
max = 0
min = 0
for ind , el in enumerate(arr):
    if el > arr[max]:
        max = ind
    elif el < arr[min]:
        min = ind

print(f"до   : {arr}")
arr[max],arr[min] = arr[min],arr[max]
print(f"после: {arr}")








    # if (el > dict["max"]):
    #     dict["max"] = el
    #     dict["max_ind"] = ind
    # elif (el < dict["min"]):
    #     dict["min"] = el
    #
