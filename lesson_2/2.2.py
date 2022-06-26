#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)


a = str(GetNumberFromUser("Введите число"))

str_chet = ""
str_nechet = ""
for i in range(0, len(a)):
    cur = a[i]

    if int(cur) % 2 == 0:
        str_chet = cur if str_chet == "" else str_chet + " , "+  cur
    else:
        str_nechet = cur if str_nechet == "" else str_nechet + " , "+ cur

print(f"Четные: {str_chet}")
print(f"Нечетные: {str_nechet}")

#Списки
#print(f"Четные: {[el for el in list(a) if int(el) % 2 == 0]}, всего {len([el for el in list(a) if int(el) % 2 == 0])} ")
#print(f"Нечетные: {[el for el in list(a) if int(el) % 2 == 1]}, всего {len([el for el in list(a) if int(el) % 2 == 1])}")
