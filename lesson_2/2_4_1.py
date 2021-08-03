from time import time

def cached(func):
    def wrapper(num, cache = {1:1,2:1}):
        current_elem = cache.get(num)
        if not current_elem:
            current_elem = func(num)
            cache.append({current_elem})
        return current_elem
    return wrapper


@cached
def fibbonachi_num(num):
    return fibbonachi_num(num - 1 ) + fibbonachi_num(num -2)

start_time = time()
print(fibbonachi_num(480))
end_time = time()
print(f'time result: {end_time- start_time}')
# 3 = (2 + 1)
# 4 = (3,2), (2,1)
# 5 = (4,3) , (3,2) , 2,1), (2,1)
# 6 = (5,4) , (4,3) , (3,2) , 2,1), (2,1), (3,2), (2,1)