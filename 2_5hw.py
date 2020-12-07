# Константы
my_list = [7, 5, 3, 3, 2]
tire = "-" * 40

# Список действий закинем в словарь
Show_Dict = {1: "Посмотреть рейтинг", 2: "Добавить число в рейтинг", 3: "Закрыть программу"}

# Реализуем некое подобие менюшки
while True:

    # Отобразим все подменю
    print("Доступные действия")
    for i in Show_Dict:
        print(f"{i} : {Show_Dict[i]}")

    print(tire)
    # Проверка что ввели цифры
    Do_task = input("Введите номер команды: ")
    if not Do_task.isdigit():
        print("Пожалуйста введите верную команду!")
        continue

    # Проверка на допустимость команды и сокращаем если float
    Do_task = int(Do_task)
    if Show_Dict.get(Do_task) is None:
        print("Пожалуйста команду из списка")
        continue

    # Обрабатываем результат
    print(f"Вы выбрали {Show_Dict[Do_task]}")

    if Do_task == 1:
        # Нужно показать текущий рейтинг
        print(tire)
        print("Текущий рейтинг:")
        print(my_list)
        print(tire)
    elif Do_task == 2:
        # Добавляем в рейтинг значение
        print(tire)
        # Запрашиваем у пользователя число которое нужно добавить в рейтинг
        while True:
            int_inp = input("Введите натуральное число для добавления в список: ")
            if not int_inp.isdigit():
                print(tire)
                continue

            int_inp = int(int_inp)
            if int_inp < 1:
                print("Натуральное пожалуйста")
                print(tire)
                continue
            # У нас есть готовое число, которое нужно добавить в рейтинг
            # 1. Сначала ищем есть ли у нас такие введенное число в списка
            if int_inp in my_list:
                # Теперь нужно добавить на позицию последнего элемента наше число
                l_index = len(my_list) - my_list[::-1].index(int_inp) - 1

                # Добавляем в массив на место последней найденно позиции
                my_list.insert(l_index + 1, int_inp)
            else:
                # 2. Не найдены элементы в списке
                max_v = max(my_list)
                min_v = min(my_list)
                if int_inp > max_v:
                    # 2.1 Если число больше любого в списке то добавляем в начало
                    my_list.insert(0, int_inp)
                elif int_inp < min_v:
                    # 2.2 Если число самое маленькое, то добавляем в конец
                    my_list.append(int_inp)
                else:
                    # Циклично обходим элементы и ищем первое значение, которое нам подходит, и на место этого элемента
                    # Вставляем число
                    for ind, value in enumerate(my_list):
                        if int_inp > value:
                            my_list.insert(ind, int_inp)
                            break
            print(tire)
            print("Рейтинг стал выглядеть как:")
            print(my_list)
            print(tire)
            break
    elif Do_task == 3:
        # Выходим из программа
        break
