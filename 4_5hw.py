from functools import reduce
from lib import multiple

print(reduce(multiple,[el for el in range(100,1001,2)]))
