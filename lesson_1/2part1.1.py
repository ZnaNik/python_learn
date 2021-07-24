from functools import reduce
def multiple(prev_el, el):
    return prev_el * el

def sum(prev_el, el):
    return prev_el + el


num = input("Введите трехзначеное число: ")

if (not num.isdigit()):
    print("Пожалуйста число введите")
    quit()
else:
    num = int(num)

check_num = int(num) / 100

if check_num > 10 or check_num < 1:
    print(f"Пожалуйста трех значное число а вы ввели: {num} знаков")
    quit()
print(f"mult: {reduce(multiple,  [int(el) for el in str(num)])}")
print(f"sum: {reduce(sum,  [int(el) for el in str(num)])}")

quit();
