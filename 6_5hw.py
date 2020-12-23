class Stationery:
    def __init__(self, _title):
        title = _title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        print("Начинаю рисовать ручкой!")

class Pencil (Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        print("Хочется порисовать карандашиком")


class Handle (Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        print("Рисую маркером")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
xxx = Stationery("Чудо Юдо")
xxx.draw()
