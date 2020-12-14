from functools import reduce
from lib import multiple

#Вобще очень плохо понял условие, реализовал как понял
def fact_range(number):
    return [i for i in range(1, number+1)]

def mass_factorial(n):
    for el in range(1,n+1):
        yield reduce(multiple, fact_range(el))

mass = mass_factorial(10)

for el in mass:
    print(el)
