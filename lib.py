def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) == 0:
            print("не ноль пожалуйста")
        else:
            return int(number)

def multiple(prev_el, el):
    return prev_el * el

