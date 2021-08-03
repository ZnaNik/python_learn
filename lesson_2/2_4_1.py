
#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
from time import time
import random
import cProfile

def les_6(max):
    start_time = time()
    arr = [random.randint(-10000,10000) for el in range(0,max)]

    min_ind = 0
    max_ind= 0
    for el in range(0, len(arr)):
        if (arr[min_ind] > arr[el]):
            min_ind = el
        elif (arr[max_ind] > arr[el]):
            max_ind = el

    sum = 0
    print(f"Минимальный индекс {min_ind} , Максимальный индекс {max_ind}")
    if (min_ind > max_ind):
        max_ind,min_ind  = min_ind, max_ind
    for el in range(min_ind+1, max_ind-1):
        sum = sum + arr[el]

    print(f"Сумма {sum}")
    print(f"Время: {time() - start_time}")


cProfile.run('les_6(500000)')
#Не совсем понял суть задания.
#Проанализировал, понял что у меня больше времени тратится на генерацию рандомных элементов , что и было в сути задания
#Как ускорить не ясно, поскольку все равно придется брать рандомный элемент на каждое значение.
#Наверное можно чуть ускорить задачу, если при генерации элементов, сразу смотреть больше он максимального или нет, и не делать
#Второй обход массива
quit()
from time import time

def cached(func):
    def wrapper(num, cache = {1:1,2:1}):
        current_elem = cache.get(num)
        if not current_elem:
            current_elem = func(num)
            cache.append({current_elem})
        return current_elem
    return wrapper


@cached
def fibbonachi_num(num):
    return fibbonachi_num(num - 1 ) + fibbonachi_num(num -2)

start_time = time()
print(fibbonachi_num(480))
end_time = time()
print(f'time result: {end_time- start_time}')
# 3 = (2 + 1)
# 4 = (3,2), (2,1)
# 5 = (4,3) , (3,2) , 2,1), (2,1)
# 6 = (5,4) , (4,3) , (3,2) , 2,1), (2,1), (3,2), (2,1)