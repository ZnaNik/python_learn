# const
max = 10
global_list = []
show_list = []

# Входные данные
while True:
    # Провесим ввести число, но смотрим на него как на строку
    var_count = str(input("введите число элементов массива: "))

    # Если ввели не число то продолжаем результата ждать
    if not var_count.isdigit():
        print("Число пожалуйста")
        continue

    # Даже если ввели float преобразуем
    var_count = int(var_count)

    # Проверим на количетсво элементов
    if (var_count <= 0):
        print("Число должно быть больше 0")
        continue

    # Ограничим массив ленью пользователя
    if (var_count > max):
        var_count = max
        print(f"Не надо больших чисел, {max} достаточно, число ограничено до {max}")
    break

# Добавлено 2 варианта обхода массива
i = 0
for i in range(var_count):
    global_list.append(input(f"Элемент[{i}] Введите любое значение: "))

print("До: ")
print(global_list)

i = 0
while i < var_count:
    # Текущее значение
    t_var = global_list[i]
    # Реализуем обмен через доп массив
    # Если элемент не четный
    if i % 2 == 1:
        show_list.insert(i - 1, t_var)
    else:
        show_list.append(t_var)

    i += 1
print("После: ")
print(show_list)
