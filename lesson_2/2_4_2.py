# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
#Запишем некий простой блок логики для собственного пояснения

#С решетом
#Построим массив из числе до некоего занчения
import cProfile

#Ждем n число от пользователя
def Eratosfen(max, n):
    arr = [el for el in range(max)]
    prost = [1]
    for i in range(2, max):
        if arr[i] != 0:
            j = i + i
            while j < max:
                arr[j] = 0
                j = j + i
            prost.append(arr[i])
            #Проверяем хватит ли нам дальше чисел
            if len(prost) == n:
                print(f"Эратосфен Числа {prost} их всего {len(prost)}")
                quit()

        i += 1

    print(f"Эратосфен не хватило простых чисел, вот сколько нашлось {prost} , их {len(prost)}")

#Делаем какой то простой метод не думая об улучшении логики
#Можно допустить, что число будет простым, если оно не делится на любое простое число, которое до этого присутствовало
#Т.е создаем массив, которые бесконечно расширяем прогоном и каждое следующее число делим по порядку на каждое из массива простых чисел
#Если наше число не разделилось ни на одно , значит простое
def My_Method(max , n):
    arr = [el for el in range(max)]
    prost = [1, 2]

    for i in range(3, max):
        simple = True
        for p_el in prost:
            if p_el >1 and arr[i] % p_el == 0:
                simple = False
                break

        if simple:
            prost.append(arr[i])
            if (len(prost) == n):
                print(f"Мой метод Числа {prost} их всего {len(prost)}")
                break

    if (len(prost) < n):
        print(f"Мой метод не хватило простых чисел, вот сколько нашлось {prost} , их {len(prost)}")

def Start(max , n):
    My_Method(max, n)
    Eratosfen(max, n)

n = int(input("Введите простое число по счету, которое надо найти: "))
max = 10000000
if (n >=  max):
    print(f"В массиве 100 чисел, всего, не надо выше {n}")
    quit()

cProfile.run('Start(max, n)')

# https://prnt.sc/1ioqt50 вставить текстом чет не вышло в строку
#видно что внезапно мой метод оказался быстрее просеивания
#По анализу мне было трудно судить, что в эратосфене заняло много времени
#Поэтому вывожу простое предположение, в моем методе быстрее завершается на коротких дистанциях, поскольку я не обхожу каждый
#Элемент до конца как в эратосфене, и не обнуляю его. Проверим это увеличив число, я вводил на первом тесте 2555

cProfile.run('Start(max, 20000)')
#Здесь уже совершенно другие показатели, и засчет деления каждого числа на список простых
#При увеличении массива я получаю сильно более отвратные результаты