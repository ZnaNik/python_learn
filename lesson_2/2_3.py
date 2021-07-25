#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        else:
            return int(number)

a = str(GetNumberFromUser("Введите число"))

str = ""
for i in range(0, len(a)):
    str = a[i] + str

print(str)
#список
#print(f"{a[::-1]}")