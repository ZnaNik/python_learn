#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

first = 32
last = 127

cur = first

str = ""
tic =0
while cur <= last:
    str = chr(cur) if str == "" else str + " " +chr(cur)
    tic += 1
    if tic == 10:
        print(str)
        str = ""
        tic = 0

    cur = cur + 1

print(str)
#Списки
# array = []
# while cur <= last:
#     array.append(chr(cur))
#     if (len(array) == 10):
#         print(array)
#         array.clear()
#
#     cur = cur +1
#
# print (array)



