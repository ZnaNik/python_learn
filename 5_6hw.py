from lib import sum, getNumFromString
from functools import reduce

with open("h6.txt", "r", encoding="utf-8") as reader:
    dict = {}
    for line in reader:
        line_split = line.split()
        # Вычленияем из строк только цифры и суммируем преобразовывая в INT (функция getNumFromString
        # потом суммируем полученные цифры в разделе, и суммируем потом все вместе, выполняется уже тут
        # Ну и удаляем знак: в конце
        dict[line_split[0][0:len(line_split[0]) - 1]] = reduce(sum, [getNumFromString(line_split[i]) for i in
                                                                     range(1, len(line_split))])

print(dict)
