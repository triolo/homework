def open_text(fname="text.txt"):
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read().lower()
        arr = text.split()
        for i, item in enumerate(arr):
            arr[i] = item.strip("""..,"'?!-""")
    return arr

def ing_count():
    ings = []
    for element in open_text():
        if element[-3:] == "ing":
            ings.append(element)
    return ings

def user_ing(arr1):
    word = input("Vvedite")
    if word[-3:] == "ing":
        k = 0
        for element in arr1:
            if element == word:
                k += 1
    else:
        print("Izvinite, vy ne pravy")
    return k

print(len(ing_count()))
print(user_ing(ing_count()))


