# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Пойдем простым путем и создадим наш класс для 16 чисел, которые будут внутри превращаться
# В 10 спокойно складываться и переводиться обратно
# Построим массив допустимых range для проверки, что число реально 16 ричное
# 0-9ABCDEF

import math

# a = 164
# print(a[0] % 16)
# HEXLIST = "0123456789ABCDEF"
# n = 164
# k = 16
# res = ""
# while n > 0:
#     result = divmod(n,k)
#     res = res + HEXLIST[result[0]]
#     n = result[1]
#     if (result[1] < k):
#         res = res + HEXLIST[result[1]]
#         break
#
# print(res)
#
# quit()
class cheat_hex:
    HEXList = ""
    double = 0
    HEX = ""

    def __init__(self, value):
        self.GetHexList()
        if type(value) == int:
            self.double = value
            self.Hex = self.ConvertToHex(self.double)
        else:
            if not self.ConvertValue(value):
                raise ("Not HexValue")
            self.HEX = value

    def GetHexList(self):
        # Дополняем цифрами
        for i in range(0, 10):
            self.HEXList = self.HEXList + str(i)

        #И до 16
        self.HEXList = self.HEXList + "ABCDEF"

    def ConvertToDecimal(self, value):
        return self.HEXList.index(value)

    def ConvertToHex(self, value):
        k=16 #Счисление
        result = divmod(value, 16)
        if result[0] <= k:
            self.HEX = self.HEX + self.HEXList[result[0]] + self.HEXList[result[1]]
        else:
            self.ConvertToHex(result[0])
            self.HEX = self.HEX + self.HEXList[result[1]]


    def ConvertValue(self, value):
        for el in range(len(value))[::-1]:
            u_el = value[el].upper()
            if not u_el in self.HEXList:
                return False
            else:
                #Поскольку идем обходом, увеличиваем каждое число на степень 16 для сохранения
                self.double = self.double + self.ConvertToDecimal(u_el)*(pow(16, (len(value) - (el+1))))

        return True

    def __add__(self, other):
        if type(other) != type(self) and type(other) != type(int):
            raise("Only hex or decimal can be summed")

        #Уже следуя логике разделяем на то, что пришло
        if type(other) == type(self):
            double = self.double+other.double
        else:
            double = self.double + other

        cHex = self.HEX  # Не знаю как getетеры сетеры делать в питоне
        self.HEX = ""
        self.ConvertToHex(double)  # Уже не хотелось выносить функцию, из вне, так да это гавнокодик
        self.HEX, cHex = cHex, self.HEX
        return cHex

    def __mul__(self, other):
        if type(other) != type(self) and type(other) != type(int):
            raise("Only hex or decimal can be multiple")

        #Уже следуя логике разделяем на то, что пришло
        if type(other) == type(self):
            double = self.double*other.double
        else:
            double = self.double * other

        cHex = self.HEX  # Не знаю как getетеры сетеры делать в питоне
        self.HEX = ""
        self.ConvertToHex(double)  # Уже не хотелось выносить функцию, из вне, так да это гавнокодик
        self.HEX, cHex = cHex, self.HEX
        return cHex
# b = 4922
# str = ""
# a = Rec_divide(b,16,str)
# print(a)
# # a = cheat_hex(492)
a = cheat_hex(100)
b = cheat_hex(100)
print(a+b)
print(a*b)
#Не понял зачем представлять как отдельные значения
#Может задумка в задании
print(list(a+b))
print(list(a*b))