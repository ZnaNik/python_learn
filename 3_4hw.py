def GetNumberFromUser(Question, minus=False):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) == 0:
            print("не ноль пожалуйста")
        else:
            return -int(number) if minus else int(number)


def pow_analog(plus_x, minus_y):
    print(f"pow {plus_x ** minus_y}")
    # Зададим переменную, чтобы она была инициализирована сразу как 1
    var_x = 1
    for i in range(abs(minus_y)):
        var_x = var_x * plus_x

    print(f"cycle {1 / var_x}")


pow_analog(GetNumberFromUser("Введите целое положительное"),
           GetNumberFromUser("Введите целое отрицательное(- не нужно писать)", True))
