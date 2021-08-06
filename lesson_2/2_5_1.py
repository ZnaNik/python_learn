# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Число пожалуйста")
        else:
           return int(number)


comp_count = GetNumberFromUser("Сколько предприятий")
quart = range(1,5)
comp_list = {}

while len(comp_list) < comp_count:
    Name = input("Введите Наименование предприятия ")
    YearValue = {}
    sum = 0
    for i in quart:
        YearValue[i] = int(input(f"Введите прибыль за квартал {i} "))
        sum = sum + YearValue[i]

    Values = {"YearQuartList": YearValue, 'YearSum':sum}
    comp_list[Name] = Values


#считаем среднюю прибыль
sum = 0
for key, value in comp_list.items():
    sum = sum + value["YearSum"]

avg_year = sum/len(comp_list)
print(f"Средняя прибыль за год {avg_year}")

#Ищем успешных и не очень , те у кого прибыль = средней, не берем
profitlist = []
shitlist = []
for key, value in comp_list.items():
    if value["YearSum"] > avg_year:
        profitlist.append(key)
    elif value["YearSum"] < avg_year:
        shitlist.append(key)
    else:
        continue
        #i dunno

print(f"Прибыль выше средней : {profitlist}")
print(f"Прибыль ниже средней : {shitlist}")

