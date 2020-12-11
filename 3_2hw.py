def input_user(Char):
    while True:
        value = input(f"Введите данные о пользователе {Char}: ").rstrip()

        if len(value) == 0:
            print("Введите хоть что нить")
        else:
            return value


def print_data(Name, SurName, Year, City, Email, Phone):
    print(f"{Name}; {SurName}; {Year}; {City}; {Email} {Phone}", end=" ")


Dict = {"Имя": "", "Фамилия": "", "Год рождения": "", "Город проживания": "", "Емаил": "", "Телефон": ""}

print("Заполните данные о себе")

for a in Dict.keys():
    Dict[a] = input_user(a)

print_data(Name=Dict["Имя"], City=Dict["Город проживания"], SurName=Dict["Фамилия"], Email=Dict["Емаил"],
           Phone=Dict["Телефон"], Year=Dict["Год рождения"])
