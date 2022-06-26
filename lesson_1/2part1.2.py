def doubleexp(n):
    b = ""
    if n< 0:
        n = n*-1;
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

def showoperation(a,b):
    print(f"Числа {a} , {b}")
    print(doubleexp(a))
    print(doubleexp(b))

def bitAnd(a,b):
    print("Битовое и")
    showoperation(a,b)
    print(doubleexp(a & b))

def bitOr(a,b):
    print("Битовое Или")
    showoperation(a,b)
    print(doubleexp(a | b))

def bitNor(a, b):
    print("Битовое Исключающее Или")
    showoperation(a, b)
    print(doubleexp(a ^ b))

def bitLeft(a,b):
    print("Побитовый сдвиг в лево")
    print(doubleexp(a))
    print(doubleexp(a << b))

def bitRight(a,b):
    print("Побитовый сдвиг вправо")
    print(doubleexp(a))
    print(doubleexp(a >> b))

#Вводим переменные
a = 5
b = 6

bitOr(a,b)
bitAnd(a,b)
bitNor(a,b)
bitLeft(a,2)
bitRight(b,2)
