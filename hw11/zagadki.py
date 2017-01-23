import random
def zagadki():
    with open("dict.csv", "r", encoding="utf-8") as f:
        text = f.read()
        arr = text.split()
        for i, item in enumerate(arr):  ##понятия не имею почему это тут работает и не работает все остальное
            arr[i] = item.strip()       ##кажется, это как-то связано с тем что создается копия строки
        diction = {}
        for item in arr:
            para = item.split(",")
            diction[para[1]] = para[0]
        keys = list(diction.keys())
        word = random.choice(keys)
        clue = diction[word]
        for i in range(len(clue)):
            print(word + " " + "...")
            popytka = input("Answer: ")
            if popytka == clue:
                print("Success")
                break
            else:
                print("Fail")
                continue
    return 0
zagadki()
