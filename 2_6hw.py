# Константы
const_char = set(("Название", "Цена", "Количество", "Ед"))
tire = "-" * 40
# Список главного меню
Show_Dict_main = {1: "Посмотреть список товаров", 2: "Добавить товар", 3: "Посмотреть аналитику",
                  4: "Выйти из программы"}

# Глобальный список
global_list = []

while True:
    # Отобразим все подменю
    print(tire)
    print("Доступные действия")
    for i in Show_Dict_main:
        print(f"{i} : {Show_Dict_main[i]}")

    print(tire)
    # Проверка что ввели цифры
    Do_task = input("Введите номер команды: ")
    if not Do_task.isdigit():
        print("Пожалуйста введите верную команду!")
        continue

    # Проверка на допустимость команды и сокращаем если float
    Do_task = int(Do_task)
    if Show_Dict_main.get(Do_task) is None:
        print("Пожалуйста команду из списка")
        continue

    # Обрабатываем результат
    print(f"Вы выбрали {Show_Dict_main[Do_task]}")
    print(tire)

    if Do_task == 1:
        if len(global_list) > 0:
            # Показываем товары
            for i in global_list:
                print(f"Строка[{i[0]}] {i[1]}")
        else:
            print("Товаров в списке нет, сначала добавьте их")
    elif Do_task == 2:
        # Формируем меню из списка характеристик заданных в начале
        Show_Dict_Add_Good = {}
        for i in const_char:
            Show_Dict_Add_Good[i] = ""

        # Добавляем два последних пункта, создать товар и отмена
        Show_Dict_Add_Good["Создать товар"] = "Добавить товар в таблицу"
        Show_Dict_Add_Good["Отмена"] = "Выйти в основной меню"

        while True:
            # Выведем этот список на экран пользователю
            for ind, (k, v) in enumerate(Show_Dict_Add_Good.items()):
                print(f"{ind + 1}. {k} : {v}")

            # Зафиксируем переменную для дальнейшего обращения
            keyList = list(Show_Dict_Add_Good.keys())
            char_len = len(Show_Dict_Add_Good)
            print(tire)
            add_command = input("Введите пункт меню: ")
            if not add_command.isdigit():
                print("Пожалуйста введите номер строки")
                continue

            add_command = int(add_command)
            if 0 == add_command or add_command > char_len:
                print("Такой строчки нету, возьмите верное значение пожалуйста")
                continue

            # Проверяем на вхыод
            if add_command == char_len:
                print(tire)
                print("Вы отменили добавление товара ")
                break
            elif add_command == char_len - 1:
                # Проводим проверку на заполненность всех характеристик

                result = True
                i = 0
                while i < len(const_char):
                    # Проверяем каждую характеристику на заполненность и выдаем ответ
                    CharName = keyList[i]
                    if Show_Dict_Add_Good[CharName] == "":
                        result = False
                        print(f"Ошибка не заполнена характеристика {CharName}")
                    i += 1

                if result:
                    print(tire)
                    print("Фиксирую товар в таблице")

                    add_dict = {}
                    for i in const_char:
                        add_dict[i] = Show_Dict_Add_Good[i]

                    # Получаем номер элемента
                    el_num = len(global_list) + 1
                    global_list.append((el_num, add_dict))

                    print(f"Товар добавлен в таблицу, его номер {el_num}")
                    break
                else:
                    print(tire)
                    print("Устраните нарушения, прежде чем фиксировать товар")

            else:
                # Выведем название характеристики
                CharName = keyList[add_command - 1]
                print(tire)

                Show_Dict_Add_Good[CharName] = input(f"Введите значение для {CharName}: ")
                print(f"Значение {Show_Dict_Add_Good[CharName]} успешно зафиксировано")
                print(tire)

        #
    elif Do_task == 3:
        if len(global_list) == 0:
            print("Нет товаров для показа аналитики")
        else:
            #Формируем массив отображения
            print("Вывожу аналитику")
            dict_char = {}
            for i in const_char:
                dict_char[i] = set()

            #Цикл в цикле для заполнения элементов
            for i in global_list:
                for i_d in dict_char:
                    dict_char[i_d].add(i[1][i_d])

            for i in dict_char:
                print(f"{i}: {dict_char[i]}")
    else:
        break