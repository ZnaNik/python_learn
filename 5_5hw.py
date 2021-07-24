from lib import sum
from functools import reduce

with open("h5_w.txt", "w", encoding="utf-8") as writer:
    # Чистим файл
    writer.truncate(0)

    input_value = input("Введите список чисел ")
    print(reduce(sum, list(map(int, input_value.split()))))
    writer.write(input_value)
