#Матрица 5x4 заполняется вводом с
# клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
from functools import  reduce
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)

def sum(a,b):
    return a+b

array = []
max_inp = 3
while(len(array) < 5):

    arr_str = []
    cur_inp = 0
    while(cur_inp < max_inp):
        inp = GetNumberFromUser(f"Введите цифру {cur_inp+1} в строке , строка в массиве {len(array) + 1}")
        cur_inp+=1
        arr_str.append(cur_inp)
    arr_str.append(reduce(sum,arr_str))
    array.append(arr_str)

print(array)
