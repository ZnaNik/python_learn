def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) <= 0:
            print("Длина отрезка больше 0!")
        else:
            return int(number)


a = GetNumberFromUser("Введите длину отрезка a")
b = GetNumberFromUser("Введите длину отрезка b")
c = GetNumberFromUser("Введите длину отрезка c")

#Проверяем что любые 2 элемента в сумме больше чем другой
my_list = [a, b,c]
if (a + b > c and  b + c > a and  a + c > b):
    print("Треугольник может существовать")
else:
    print("Сумма любых двух сторон больше третьей, такого треугольника существовать не может")
    quit()

if (a == b == c):
    print(" Треугольник равносторонний")
elif len(list(set(my_list))) < len(my_list):
    print("треугольник равнобедренный")
else:
    print("треугольник разносторонний")
