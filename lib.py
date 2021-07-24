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

def s_sum(el, prev_el):
    return el+prev_el if len(prev_el) == 0 else el+prev_el + "\n"

#Получение только цифр из строки
def getNumFromString(in_string):
    list = [i for i in in_string[::-1] if i.isdigit()]
    if len(list) == 0:
        return 0
    else:
        return int(reduce(sum, list))

def CheckIsMatrix(matrix):
    if type(matrix) != list:
        raise TypeError("Пожалуйста матрицу")

    # Проверим сходимость матрицы, достраивать не будем
    len_need = 0
    for ind, i in enumerate(matrix):
        if type(i) != list:
            raise TypeError(f" {matrix[ind]} is not matrix")

        #Зададим базовое соответствие
        if len_need == 0:
            len_need = len(i)
        elif len_need != len(i):
            raise TypeError(f" {matrix[ind]} has wrong lenght")

#Считается что сюда уже попали матрицы
def MatrixIsEqual(matrix_1, matrix_2):

    if len(matrix_1) != len(matrix_2):
        raise ValueError("Not equal matrix")

    #Проверки для первого элемента достаточно
    if (len(matrix_1[0]) != len(matrix_2[0])):
        raise ValueError("Not equal matrix")

