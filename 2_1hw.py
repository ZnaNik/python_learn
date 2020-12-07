# Инициализируем глобальный список
t_global = []

# 1. Формируем базовые типы для создания массива потом
t_int = 2
t_float = 2.25
t_string = "Привет"
t_boolean = True
t_list = [2, 25, "tt"]
t_set = (t_int, t_float, t_string)

# Заполняем массив всеми типами
t_global.append(t_int)  # int
t_global.append(t_float)  # float
t_global.append(2 + 25j)  # complex
t_global.append(t_string)  # string
t_global.append(t_list)  # list
t_global.append((t_int, t_string, t_boolean, t_list, t_list.reverse()))  # tuple 2 list inverted
t_global.append(t_set)  # set
t_global.append(frozenset(t_set))  # frozenset
t_global.append({1: t_int, 2: t_list, "3": t_set})  # dictionary
t_global.append(False)  # bool
t_global.append(b'(f{t_string})')  # byte
t_global.append(bytearray(b"Welcome to byte world"))  # bytearray
t_global.append(None)  # None
t_global.append(Exception("Expection is wonderful"))  # expection

# Заполняем глобальный список

for m_type in t_global:
    print(f"Value: {m_type} type: ({type(m_type)})")
