#7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

from functools import reduce

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста натуральное число")
        elif int(number) == 0:
            print("0 это целое число")
        else:
            return int(number)


def sum_f(a,b):
    return a+b;

def form(n):
    return int(n*(n+1)/2)

n = GetNumberFromUser("Введите натуральное число, для проверки равенства")

res_1 = 0
for el in range (1, n+1):
    res_1 = sum_f(res_1, el)

res_2 = form(n)
print(f"Первая часть: {res_1} = {res_2} Вторая часть" )
print(f"{'Условие доказано' if res_2 == res_1 else 'Условие сломалось, и не доказано'}")
#Списки
#+1 делается, чтобы само число тоже попало
# res_1 = int(reduce(sum,[el for el in range(n+1)]))
#res_2 = form(n)
# print(f"Первая часть: {res_1} = {res_2} Вторая часть" )
# print(f"{'Условие доказано' if res_2 == res_1 else 'Условие сломалось, и не доказано'}")