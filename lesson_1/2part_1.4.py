import random


def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) == 0:
            print("не ноль пожалуйста")
        else:
            return int(number)


def GetFloatFromUser(Question):
    while True:
        number = input(Question + "?: ")
        try:
            return float(number)
        except:
            print("Пожалуйста вещественное число")


def GetSymbolFromUser(Question):
    while True:
        symbol = input(Question + "?: ")
        if (len(symbol) != 1):
            print("Пожалуйста 1 символ!")
        else:
            return ord(symbol)


def Compare(Min, Max):
    if Min >= Max:
        print("Верхняя граница должна быть больше нижней")
        quit()


# случайное целое число;
Min = GetNumberFromUser("Введите нижнюю границу целого числа: ")
Max = GetNumberFromUser("Введите верхнюю границу целого числа: ")
Compare(Min, Max)
print(random.randint(Min, Max))

# случайное вещественное число;
Min = GetFloatFromUser("Введите нижнюю границу вещественного числа: ")
Max = GetFloatFromUser("Введите верхнюю границу вещественного числа: ")
Compare(Min, Max)
print(random.uniform(Min, Max))

# случайный символ.
Min = GetSymbolFromUser("Введите 1 символ нижний: ")
Max = GetSymbolFromUser("Введите 2 символ верхний: ")
Compare(Min, Max)
print(chr(random.randint(Min, Max)))
