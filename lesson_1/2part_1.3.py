# y=kx+b
#
# y1 = kx1+b
# y2 = kx2+b
#
# b = y1-kx1
# b = y2 - kx2
# y1-kx1 = y2-kx2
# kx2-kx1 = y2 - y1
#
# !!k = (y2 - y1) / (x2 - x1)
# b = y1 - (y2 - y1 / x2 - x1 ) * x1
# b = y1 - (x1* y2 - x1 * y1) / x2 - x1
# b = x2y1 - x1y1 - x1y2 + x1y1 / x2 - x1
# !!b = x2y1 - x1y2/x2-x1

print("уравнение y = kx+b")
x1 = float(input('x1 '))
y1 = float(input('y1 '))
x2 = float(input('x2 '))
y2 = float(input('y2' ))
if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    print(f'Уравнение y = {k}x + {b}')
else:
    #Достаточно провести прямую, независимо от y
    print(f'Уравнение x = {x1}')
