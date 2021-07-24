#Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)

def OurYear(Year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

year = GetNumberFromUser("Введите год")

if (OurYear(year)):
    print("Год високосный")
else:
    print("Год не високосный")
