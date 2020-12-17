from lib import GetAnyValue, sum
import json
from functools import reduce

with open("h3.txt", "r", encoding="utf-8") as reader:
    Dict = {}
    datalist = reader.read().split("\n")
    #формируем словарь на расчет
    for i in datalist:
        data = i.split()
        Dict[data[0]] = int(data[1])


#Расчет зп
print(f"У следующих сотрудников зп меньше 20000: {[user for user, salary in Dict.items() if salary < 20000]}")
print(f"Средний доход: {(reduce(sum,[salary for salary in Dict.values()]))/len(Dict)}")
