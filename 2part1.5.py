def GetAlphabeLetterFromUser(Question):
    while True:
        symbol = input(Question + "?: ")
        if (len(symbol) != 1):
            print("Пожалуйста 1 символ!")
        elif(not symbol.isalpha()):
            print("Пожалуйста букву алфавита")
        else:
            return symbol.lower()


def GetAlphabet(start_symbol, last_symbol):
    start_symbol = ord(start_symbol)
    last_symbol = ord(last_symbol)
    curorder = start_symbol
    alph = {}

    while curorder <= last_symbol:
        alph[chr(curorder)] = curorder
        curorder = curorder + 1

    return alph

def LetterInAlphabet(alphabet, letter):
    return alphabet.get(letter) != None


def LetterPositionInAlphabet(alphabet, letter):
    return list(alphabet.keys()).index(letter)+1


#Построим словарик английского и русского алфавита
rus_alph = GetAlphabet("а", "я")
eng_alph = GetAlphabet("a", "z")
a = GetAlphabeLetterFromUser("Введите первую букву")
b = GetAlphabeLetterFromUser("Введите вторую букву")

#Проверяем алфавит первой буквы
IsRussian = LetterInAlphabet(rus_alph, a)

#Теперь смотрим чтобы и вторая была там же
if (LetterInAlphabet(rus_alph,b) != IsRussian):
    print("Буквы должны быть в одном алфавите")
    quit()
#Еще можно проверку на соответствие кодов символов, но решил не заморачиваться

if (IsRussian):
    curalph = rus_alph
else:
    curalph = eng_alph

a_pos = LetterPositionInAlphabet(curalph, a)
b_pos = LetterPositionInAlphabet(curalph, b)

print(f"Позиция 1 буквы: {a_pos}")
print(f"Позиция 2 буквы: {b_pos}")
print(f"Между ними: {abs(a_pos - b_pos)} букв")





#LetterInSameAlphabet(rus_alph, a, b))

#определяем что в русском алфавите
#print(rus_alph.get(a) + 1)