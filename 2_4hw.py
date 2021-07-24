# Максимальная длина
str_max_len = 10

while True:
    str_inp = input("Введите несколько слов с пробелами: ")
    # Уберем лишние пробелы
    str_inp = str_inp.rstrip()
    a = str_inp.split(" ")

    # 1 Учитывает чтобы вводили хотя бы 2 слова с пробелом
    if len(a) > 1:
        break

    print("Несколько слов пожалуйста!")

# Блок вывод через переменную
print("Переменная")
t = 0
for i in a:
    print(t, i[0:str_max_len - 1])
    t += 1

# Блок вывода через enumerate
print("Enumerate")
for ind, i in enumerate(a):
    print(ind, i[0:str_max_len - 1])

# Блок вывода через индексы
print("Индексы")
for i in a:
    print(a.index(i), i[0:str_max_len - 1])
