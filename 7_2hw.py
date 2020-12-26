from abc import ABC, abstractmethod


class WareHouse:
    Stock = []

    def ClearStock(self):
        self.Stock = []

    def __add__(self, other):
        self.Stock.append(other)

    def AllFabric(self):
        need = 0

        for i in self.Stock:
            need = need + i.Fabric

        print(f"Всего нужно ткани на {len(self.Stock)} предмета одежды {need} м")


class clothes(ABC):

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name;

    @name.getter
    def name(self):
        return self.__name + "(tm)"


    @property
    def Fabric(self):
        return self._fabric

    def NeedFabric(self):
        print(f"Нужно ткани на {self.name} {self._fabric} м")

    @abstractmethod
    def SetSize(self):
        pass


class coat(clothes):
    def __init__(self, m_name):
        self.name = m_name

    def SetSize(self, size):
        self._fabric = size / 6.5 + 0.5

class costume(clothes):
    def __init__(self, m_name):
        self.name = m_name

    def SetSize(self, growth):
        self._fabric = growth * 2 + 0.3

a = coat("PALTO")
b = costume("COSTUMCHIK")
a.SetSize(13)
b.SetSize(4)
a.NeedFabric()
b.NeedFabric()
My_Stock = WareHouse()
My_Stock+a
My_Stock+b
My_Stock.AllFabric()
