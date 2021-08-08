#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import sys
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)


a = str(GetNumberFromUser("Введите число"))
#Вариант 1
str_chet = ""
str_nechet = ""
for i in range(0, len(a)):
    cur = a[i]

    if int(cur) % 2 == 0:
        str_chet = cur if str_chet == "" else str_chet + " , "+  cur
    else:
        str_nechet = cur if str_nechet == "" else str_nechet + " , "+ cur
24
print(f"Четные: {str_chet}")
print(f"Нечетные: {str_nechet}")
print(f"№1 Четные память: {sys.getrefcount(str_chet)}")
print(f"№1 Нечетные память: {sys.getrefcount(str_nechet)}")
#Вариант 2
#44Списки
str_chet =  [el for el in list(a) if int(el) % 2 == 0]
str_nechet = [el for el in list(a) if int(el) % 2 == 1]
print(f"Четные: {str_chet}")
print(f"Нечетные: {str_nechet}")
print(f"№1 Четные память: {sys.getrefcount(str_chet)}")
print(f"№1 Нечетные память: {sys.getrefcount(str_nechet)}")
#test _ 1
# Введите число?: 24242521
# Четные: 2 , 4 , 2 , 4 , 2 , 2
# Нечетные: 5 , 1
# №1 Четные память: 2
# №1 Нечетные память: 2
# Четные: ['2', '4', '2', '4', '2', '2']
# Нечетные: ['5', '1']
# №1 Четные память: 2
# №1 Нечетные память: 2
#
#test_2
# Введите число?: 24
# Четные: 2 , 4
# Нечетные:
# №1 Четные память: 2
# №1 Нечетные память: 63
# Четные: ['2', '4']
# Нечетные: []
# №1 Четные память: 2
# №1 Нечетные память: 2
#
#
#test_3
# Введите число?: 31
# Четные:
# Нечетные: 3 , 1
# №1 Четные память: 63
# №1 Нечетные память: 2
# Четные: []
# Нечетные: ['3', '1']
# №1 Четные память: 2
# №1 Нечетные память: 2
#
#Python 3.9 OS 64-x
#Полагаю, что с obj gen сразу идет аккуратная обработка памяти, а после первого метода
#Остается куча мусора
