# Переменные
age = int(input("Введите ваш возраст?: "))
name = input("Ваше имя? ")
time = int(input("Желаемый срок займа в месяцах: "))
sum = float(input("Введите сумму сайма: "))

# Константы
currency = "руб."
# Годовой процент
percent = 1.2

# Проверяем возможность выдачи кредита
if age > 18 or age < 70:
    result = True
else:
    result = False

# Проверка на суммы
if time <= 0 or sum <= 0:
    result = False
else:
    # Высчитаем сколько полных лет начислять процент
    years = time // 12
    # Считаем конечную сумму по годам
    # Также заметил странную разницу к пример
    # 1.2 * 1.2 * 1.2 = 1.728
    # 1.2 ** 3 = 1.7279999999999998
    year_payment = percent ** years * sum
    # Считаем начисленную сумму за неполные года
    other_sum = (sum / 12) * (time % 12)
    payment = year_payment + other_sum

    # Приводим payment к округлению двух знаков
    payment = int(payment * 100 ) / 100
    
# Вывод результата
if result:
    print(f"Уважаемый {name}, вам одобрен кредит, вам нужно будет вернуть {payment} {currency} ")
else:
    print(f"Уважаемый {name}, кредит вам не одобрен")
