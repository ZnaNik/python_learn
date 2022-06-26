#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
import random

arr = [random.randint(-50,100) for el in range(0,10)]

min_ind = 0
max_ind= 0
for el in range(0, len(arr)):
    if (arr[min_ind] > arr[el]):
        min_ind = el
    elif (arr[max_ind] > arr[el]):
        max_ind = el

sum = 0
print(arr)
print(f"Минимальный индекс {min_ind} , Максимальный индекс {max_ind}")
if (min_ind > max_ind):
    max_ind,min_ind  = min_ind, max_ind
for el in range(min_ind+1, max_ind-1):
    sum = sum + arr[el]


print(f"Сумма {sum}")