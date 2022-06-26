import random

#Генерируем массив случайных числе
arr = [random.randint(-10,10) for el in range(0,50)]
m_dict = {}

for el in arr:
    if m_dict.get(el) == None:
        m_dict[el] = 0

    m_dict[el] = m_dict[el] + 1

max_ind = 0
for item in m_dict:
    if (m_dict[max_ind] < m_dict[item]):
        max_ind = item

print(f"{max_ind} встречается {m_dict[max_ind]} раза")
#Я абсолютно не понял, почему мне выдает ошибку max(m_dict.values) поэтому его нашел в цикле
#print(f"{max(dict.values())}")
#print(max(dict.values()))