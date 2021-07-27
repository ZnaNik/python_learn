#Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

#Генерируем случайную матрицу
arr = []
matrix_max = random.randint(3,10)
for el in range(0, random.randint(2,5)):
    arr.append([random.randint(-50,100) for el in range(0,matrix_max)])

max_r = 0

for el in arr:
    min_r = min(el)

    if max_r < min_r:
        max_r = min_r

print(arr)
print(f"Максимальный среди минимальных {max_r}")

