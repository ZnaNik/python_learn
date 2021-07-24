income_sum = float(input("Введите прибыль фирмы: "))
if income_sum < 0:
    print("Отрицательного дохода быть не может: ")
    quit()

outcome_sum = float(input("Введите ваши издержки: "))
if outcome_sum < 0:
    # Превратим ее в полжоительное значение, для дальнейшего упрощения
    outcome_sum = outcome_sum * (-1)

if income_sum > outcome_sum:
    # Прибыль
    plus = income_sum - outcome_sum;
    plus_percent = income_sum * 100 / outcome_sum
    print(f"Поздравляю, ваша компания успешна, ваша рентабельность составляет : {plus_percent} %")
    people = int(input("Введите численность сотрудника вашей компании: "))

    if people <= 0:
        print("Введите верные данные, у вас никто не работает, а вы сами?")
    else:
        print(f"Каждый сотрудник в отдельности принес вам: {int(plus / people)} руб.")
elif income_sum < outcome_sum:
    # Убыток
    print("Ваши финансовые показатели далеки от идеала, ваша фирма убыточна")
else:
    # Баланс
    print("Ваши доходы равны вашим расходам, но утерянное время бесценно")