class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print(f"{self._name} поехала")
        pass

    def stop(self):
        print(f"{self._name} остановилась")

    def turn(self, Direction):
        print(f"{self._name} повернула на {Direction}")

    def show_speed(self):
        print(f"Скорость {self._speed} у {self._name}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._speed > 60:
            print(f"Превышение скорости у {self._name}")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self._speed > 40:
            print(f"Превышение скорости у {self._name}")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# Создал экземпляры класса
Matiz = TownCar(70, "brown", "Matiz")
Audi = SportCar(200, "red", "QX 25")
MX25 = WorkCar(50, "white", "Mx123421")
Lada = PoliceCar(50, "blue", "Lada vesta")

# Доступ к атрибутам
print(Matiz._name)
print(Audi._color)
# Методы и результат
Matiz.show_speed()
Lada.show_speed()
MX25.show_speed()
Audi.show_speed()
