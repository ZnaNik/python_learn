#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста натуральное число")
        else:
            return str(number)

while (True):
    num = GetNumberFromUser("Введите последовательность чисел")
    if (len(str(num)) < 3):
        print("Введите пожалуйста число длинее 2-х знаков")
    else:
        break

find_num = GetNumberFromUser("Введите число, которую нужно найти")
count = 0
for el in range(0,len(num)):
    if num[el] == find_num:
        count += 1

print(f"Число {find_num} встретилось: {count} раз")

#Списки
#print(f"{len([el for el in str(num)[::1] if int(el) == find_num])} раз встретилось это число ")