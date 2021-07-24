from lib import GetAnyValue

writer = open("h1.txt", "w", encoding="utf-8")
while True:
    value = GetAnyValue()
    if len(value) == 0:
        break
    writer.writelines(value + "\n")

writer.close()
