import json

# Название форма собственности выручка издержки
# Создаем эталонный словарь и заполняем его
Dict_Etalon = {"Название": "", "ФормаСобственности": "", "Выручка": "", "Издержки": ""}
global_list = []
DictKeys = list(Dict_Etalon.keys())
# Список словарей всех фирм
firm_list = []
# Словарь прибыли
Dict_Plus = {}

with open("h7.txt", "r", encoding="utf-8") as reader:
    plus_avg = 0
    for line in reader:
        line_split = line.rstrip().split()
        # Копируем эталонный словарь
        Dict = Dict_Etalon.copy()

        # Заполним словарь, для значений потом не используется, но для пояснения так понятнее
        for ind, i in enumerate(line_split):
            Dict[DictKeys[ind]] = int(i) if i.isdigit() else i

        plus_firm = Dict["Выручка"] - Dict["Издержки"]

        # Считаем даные для средней прибыли
        if plus_firm > 0:
            plus_avg = plus_avg + plus_firm

        Dict_Plus[Dict["Название"]] = plus_firm
        # Добавим фирму в главный лист
        firm_list.append(Dict)

global_list.append(Dict_Plus)
global_list.append({"average_profit": (plus_avg / len(firm_list))})
print(global_list)

# Для тестов лучше не перезаполнять главный файл поэтмоу запись пойдет в другой файл
with open("h7_result.txt", "w", encoding="utf-8") as writer:
    json.dump(global_list, writer)
