#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

#Генерируем массив случайных числе
arr = [random.randint(-50,100) for el in range(0,50)]
#Насколько я понял максимальный отрицательный элемент к примеру -5 -6 -7 это будет -7 т.е по модулю ан е по сравнению
# с другими

min = arr[0]
min_ind = 0
for ind, el in enumerate(arr):
    if el<0 and abs(el) > abs(min):
        min = el
        min_ind = ind

print(arr)
print(f"min_ind {min_ind} , min {min}")

#Я абсолютно не понял, почему мне выдает ошибку max(m_dict.values) поэтому его нашел в цикле
#print(f"{max(dict.values())}")
#print(max(dict.values()))