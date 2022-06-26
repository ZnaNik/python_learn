#. # В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) > 100:
            print("генератор случайных чисел, загадывает от 0 до 100, зачем такое большое число, введите меньше")
        else:
            return int(number)

greatRandom = random.randint(0,100)
maxcount = 10
falsecount = 0
while (True):
    if falsecount == maxcount:
        print(f"Вот какое было число {greatRandom}")
        quit()

    num = GetNumberFromUser("Попробуйте угадать число")

    if (num == greatRandom):
        print("Вы угадали число")
        quit()
    else:
        falsecount = falsecount+1
        print(f"Осталось попыток {maxcount - falsecount}")
        print("Введенное число больше загаданного" if num > greatRandom else "Введное число меньше загаданного")



