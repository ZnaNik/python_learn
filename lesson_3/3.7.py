#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

arr = [random.randint(-50,100) for el in range(0,10)]
#Определим массив
print(arr)
min_1 = min(arr)
arr.pop(arr.index(min_1))
min_2 = min(arr)

print(f"{min_1} , {min_2}")