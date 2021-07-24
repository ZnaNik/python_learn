# Очевидным бы решением было бы сделать https://pypi.org/project/googletrans/
# Но мы пойдем через слово замену
Dict_equals = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("h4.txt", "r", encoding="utf-8") as reader:
    with open("h4_w.txt", "w", encoding="utf-8") as writer:
        for line in reader:
            l_split = line.rstrip().split()
            string = Dict_equals[l_split[0]] + line.replace(l_split[0], "")
            print(string)
            writer.write(string)
