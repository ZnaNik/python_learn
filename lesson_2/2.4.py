from functools import reduce

#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)


def sum_f(a,b):
    return a+b;

a = GetNumberFromUser("Введите число элементов массива")

cur_pos = 0
number = -2
sum = 0
while cur_pos <= a:
    number = number * - 0.5
    cur_pos += 1
    sum = sum_f(sum, number)

print(sum)

#Список для reduce
#num = -2
#n = []
#while (len(n) < a):
#    num = num * -0.5
#    n.append(num)

#print(reduce(sum, n))

