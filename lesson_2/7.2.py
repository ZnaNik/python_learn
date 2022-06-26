# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def sliyanie_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2  # Даже если останется остаток уйдет в право
        left = sliyanie_sort(array[:mid])
        right = sliyanie_sort(array[mid:])
        return compare(left, right)


# array = [10, 7, 9 ,4, 6, 3, 1]
def compare(left, right):
    res = []
    # В результате должен остаться только один массив а левый и правый исчезнуть
    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            res.append(right.pop(0))
        elif len(right) == 0:
            res.append(left.pop(0))
        else:
            if (left[0] > right[0]):
                res.append(right.pop(0))
            else:
                res.append(left.pop(0))
    return res


array = ([random.randint(0, 50) for el in range(0, 50)])

# Попробуем написать самостоятельно не воруя код из гугла

# array = [10, 7, 9 ,4, 6, 3, 1]
print(sliyanie_sort(array))
