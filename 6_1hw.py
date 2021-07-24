from enum import Enum
from datetime import datetime
import time


class Colors(Enum):
    Красный = 1
    Желтый = 2
    Зеленый = 3


class TrafficLight:
    __color = Colors.Красный

    def running(self):
        # Получим первоначальное время запуска
        __color = Colors.Желтый
        start_time = datetime.now()
        while True:

            # Ждем секунду
            time.sleep(1)
            if len(input("Введите пустую строку если хотите сломать этот фонарик ")) == 0:
                print("Ну вот вы сломали светофор")
                break
            # r-y(7), #y-g(2), #g-r(6)
            # Отсюда я могу делать вывод что цикл это 7+2+6=15
            # Значит мне нужно посчитать сколько прошло времени с последнего цикла и тогда я смогу точно определить
            # Мой цвет
            s_passed = (datetime.now() - start_time).seconds
            if s_passed % 15 <= 7:
                self.__color = Colors.Красный
            elif s_passed % 15 <= 9:
                self.__color = Colors.Желтый
            else:
                self.__color = Colors.Зеленый

            print(f"Прошло {s_passed} секунд с момента запуска светофора")
            print(f"Я думаю цвет {self.__color}")

    def getColor(self):
        print(f"На сломанном светофоре застыл цвет {self.__color}")

#Код выполнения
Light = TrafficLight()
Light.running()
Light.getColor()
