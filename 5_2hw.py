from lib import GetAnyValue

with open("h2.txt", "r+", encoding="utf-8") as writer:
    writer.truncate(0)
    # Сохраняем несколько строк
    while True:
        value = GetAnyValue()
        if len(value) > 0:
            writer.write(value + "\n")
        else:
            writer.seek(0)
            List = writer.read().split("\n")
            # Удалим последнее значение, т.к оно будет всегда пустым
            List.pop(len(List) - 1)
            print(f"Всего строк: {len(List)}")

            for ind, i in enumerate(List):
                print(f"Слов в строке[{ind + 1}]: {len(i.split())}")
            break
