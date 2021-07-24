def GetAlphabet(start_symbol, last_symbol):
    start_symbol = ord(start_symbol)
    last_symbol = ord(last_symbol)
    curorder = start_symbol
    alph = {}

    while curorder <= last_symbol:
        alph[chr(curorder)] = curorder
        curorder = curorder + 1

    return alph

def GetNumberFromUser(Question):
    while True:
        number = input(Question + "?: ")
        if not number.isdigit():
            print("Пожалуйста число")
        elif int(number) <= 0:
            print("Номер буквы строго больше 0")
        else:
            return int(number)

def GetLetterFromAlphabet(alphabet, num):
    if num > len(alphabet):
        return "не найдено"
    else:
        return "буква: " + list(alphabet.keys())[num-1]


rus_alph = GetAlphabet("а", "я")
eng_alph = GetAlphabet("a", "z")

#Ищем в двух алфавитах
num = GetNumberFromUser("Введите номер буквы в алфавите")

print(f"В русском алфавите это {GetLetterFromAlphabet(rus_alph, num)}")
print(f"В английском алфавите это {GetLetterFromAlphabet(eng_alph, num)}")
