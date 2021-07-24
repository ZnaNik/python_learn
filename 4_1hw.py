from sys import argv

def check_float_arg(value):
    try:
        value = float(value)
        return value
    except:
        print(f"{value} not float")

    return False

#Код программы
patch, hours, hour_payment, premium = argv
hours = check_float_arg(hours)
hour_payment = check_float_arg(hour_payment)
premium = check_float_arg(premium)

#Ранее могло вернуться булево, также проверка проверит и нулевое значение
if not(hours and premium and hour_payment):
    print("PLS INPUT Correct data!")
else:
    print(f"Зарплата: {float(hours) * float(hour_payment) + float(premium)}, руб.")
