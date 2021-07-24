#Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)


a = GetNumberFromUser("1 число")
b = GetNumberFromUser("2 число")
c = GetNumberFromUser("3 число")

array = [a, b, c]
if len(list(set(array))) < len(array):
    print(" по условию вводим 3 разных числа")
    quit()

#Определяем самое большее число и убираем его из сравнения
array.remove(max(*[a,b,c]))
if (array[0] > array[1]):
    print(array[0])
else:
    print(array[1])