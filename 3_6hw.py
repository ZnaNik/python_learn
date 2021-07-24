def int_func(word):
    return word.capitalize();


def UserInput():
    return input("Пожалуйста введите строку разделенную пробелами, или '/' чтобы закончить: ").rstrip().split()


def ExitCheck(value):
    return value == "/"


m_break = False
while not m_break:

    words = UserInput()

    i = 0
    while i < len(words):

        if ExitCheck(words[i]):
            m_break = True
            break

        print(int_func(words[i]))
        i += 1
