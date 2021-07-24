def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста натуральное число")
        else:
            return int(number)


def Max_3(int_1, int_2, int_3):
    print(sum([int_1, int_2, int_3]) - min(int_1, int_2, int_3))


Max_3(GetNumberFromUser("Число 1"), GetNumberFromUser("Число 2"), GetNumberFromUser("Число 3"))
