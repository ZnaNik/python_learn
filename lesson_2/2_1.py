def GetNumberFromUser(Question, nonzero = False):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif nonzero and int(number) == 0:
            print("Делить на 0 нельзя")
        else:
            return int(number)

def GetOperationFromuser():
    dict = {}
    #Полагаю допустимый список иначе мне это нужно прописывтаь так в коде
    dict["+"] = plus
    dict["-"] = minus
    dict["/"] = divide
    dict["*"] = multiple
    dict["0"] = exit

    while (True):
        print("Список допустимых операций")
        for key, value in dict.items():
            print(key)

        command = input("Введите вид операции")

        if (len(command) != 1):
            print("Пожалуйста введите 1 знак")
        else:
            com = dict.get(command)
            if (com == None):
                print("Допустимую команду пожауйста из списка")
            else:
                return com


def exit():
    quit()

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiple(a,b):
    return a*b

while True:
    operation = GetOperationFromuser()

    if (operation == exit):
        exit()

    a = GetNumberFromUser("Введите число 1")
    b = GetNumberFromUser("Введите число 2",  (operation == divide))

    print(operation(a,b))
