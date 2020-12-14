from lib import GetNumberFromUser
from itertools import count, cycle

# _1 начиная с указанного
num_start = GetNumberFromUser("Введите число")

for el in count(num_start):
    print(el)

    if el > num_start + 10:
        break

# Повторяющий элементы списка определенного
my_list = [5, 32, 4, 8, 146, 132, 4, 5, 7, 38, 6, 9, 3, 4, 2]
c = 0
for el in cycle(my_list):
    if c > 100:
        break
    print(el)
    c += 1
