#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

from functools import reduce
#array = []

def sum_f(a,b):
    return int(a)+int(b)


str = ""

while (True):
    sign = input("Введите число, для завершения введите / :")

    if sign == "/":
        break

    if not sign.isdigit():
        print("Пожалуйста число")
        continue

    str = sign if str == "" else str + " " +sign

str = str + " "
sum = 0
cur_num = ""
max = 0
max_num = ""
for el in range(0, len(str)):

    if str[el] == " ":
        if (sum >= max):
            max = sum
            max_num = cur_num

        sum = 0
        cur_num = ""
    else:
        sum = sum_f(sum, int(str[el]))
        cur_num = cur_num + str[el]

print(f"Число: {max_num} сумма цифр: {max}")


#Списки
#Выводим максимальное число по сумме цифр
# if (len(array) > 0):
#     print(f" Максимальная сумма цифр в введенных числах {max([int(reduce(sum,el[::1])) for el in [list(str(el)) for el in array]])}")
# else:
#     print("Массив пуст, считать нечего")


