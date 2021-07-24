def UserInput():
    return input("Пожалуйста введите строку разделенную пробелами, или '/' чтобы закончить: ").rstrip().split()


def ExitCheck(value):
    return value == "/"


def Execute_list(n_list):
    if n_list is None:
        return (0, True)

    ind = 0
    m_break = False;
    while ind < len(n_list):
        i = n_list[ind]
        if not i.isdigit():
            m_break = ExitCheck(i)
            # Я несовсем понял условие, нужно ли если случился выход не считать
            # Дальнейшие числа, ну да ладно оставлю подсчет, если что тут будет условие if(mbreak) break
            n_list.pop(ind)
        else:
            n_list[ind] = int(i)
            ind += 1

    return m_break, sum(n_list)


# Тело программы
n_list = ""
all_sum = 0

while True:
    n_list = UserInput()
    res = Execute_list(n_list)
    all_sum = all_sum + res[1]

    print(all_sum)
    if res[0]:
        break
