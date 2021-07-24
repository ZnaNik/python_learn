from functools import reduce

# Ввод число от пользователя
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) == 0:
            print("не ноль пожалуйста")
        else:
            return int(number)


# Ввод любого значения от пользователя
def GetAnyValue():
    return input("Введите любое значение, для выхода введите пустую строку ").rstrip()


# Умножение
def multiple(prev_el, el):
    return prev_el * el


# Сложение
def sum(prev_el, el):
    return el + prev_el

#Получение только цифр из строки
def getNumFromString(in_string):
    list = [i for i in in_string[::-1] if i.isdigit()]
    if len(list) == 0:
        return 0
    else:
        return int(reduce(sum, list))

