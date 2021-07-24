def Division(int_1, int_2):
    if int_2 == 0:
        return "бесконечность, а не надо было делить на 0!"
    else:
        return int_1/int_2

def GetNumberFromUser(Question):
    while True:
        number = input(Question+"?: ")
        if not number.isdigit():
            print("Пожалуйста натуральное число")
        else:
            return int(number)

print(f"Результат: {Division(GetNumberFromUser('Введите делимое'),GetNumberFromUser('Введите делитель'))}")