# Я плохо понял условие про словарь
# Делаю предположение что это словарь в словаре по позициям
def get_wage(wage, bonus):
    return {"wage": wage, "bonus": bonus}


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + " " + self.surname

    # Вариант через переопределение
    def get_total_income(self):
        return super().get_total_income()


Income = {10000: 1000, 20000: 2000, 30000: 3000, 40000: 4000}

Position_dict = {}
Position_dict["Начальник смены"] = get_wage(150000, 20000)
Position_dict["Мастер"] = get_wage(50000, 5000)
Position_dict["Стажер"] = get_wage(30000, 2000)

Pos1 = Position("Vasilya", "Alibabaevich", "Начальник смены", Position_dict["Начальник смены"])
Pos2 = Position("Anfisa", "Rukastova", "Стажер", Position_dict["Стажер"])

print(Pos1.get_full_name())
print(Pos1.get_total_income())

print(Pos2.get_full_name())
print(Pos2.get_total_income())
