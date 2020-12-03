num = int(input("Введите число: "))

high_nun = 0

if (num <= 0):
    print("Неверное число")
else:
    # К примеру число 1234
    # Делим это на 10 получаем конечную цифру остатка - 4
    while num > 0:
        current = num % 10
        if (current > high_nun):
            high_nun = current
        num = int(num // 10)

print(high_nun)
