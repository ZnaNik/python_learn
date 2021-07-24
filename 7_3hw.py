from functools import reduce
from lib import sum


class Organic_cell:
    def __init__(self, num_cells):
        self.Cells = num_cells

    @property
    def Cells(self):
        return self.__num_cells

    @Cells.setter
    def Cells(self, Cells):
        self.__num_cells = Cells

    def __add__(self, other):
        self.Cells = self.Cells + other.Cells

    def __sub__(self, other):
        self.Cells = 0 if (self.Cells - other.Cells) < 0 else self.Cells - other.Cells

    def __mul__(self, other):
        self.Cells = self.Cells * other.Cells

    def __truediv__(self, other):
        self.Cells = int(self.Cells // other.Cells)

    def __str__(self):
        return str(self.Cells)

    def make_order(self, row):
        rows = self.Cells // row
        a = [r"*" * row for el in range(0, rows)]
        a = list(map(lambda x: x + "\\n", a))
        if self.Cells % row > 0:
            a.append(self.Cells % row * "*")
        else:
            a[len(a) - 1] = str.replace(a[len(a) - 1], "\\n", "")

        b = reduce(sum, a[::-1])
        print(b)


# Сложение
a = Organic_cell(15)
b = Organic_cell(10)
a + b
print(f"Сложение {a}")
# Вычитание
c = Organic_cell(20)
a - c
print(f"Вычитание {a}")
# Вычитание Меньше 0 клеток не будет
a - c
print(f"Вычитание {a}")
# Добавим клеток
a + b
d = Organic_cell(2)
a * d
print(f"Умножение {a}")
# Деление
e = Organic_cell(12)
a / e
print(f"Деление {a}")
# make order
a = Organic_cell(15)
a.make_order(5)
