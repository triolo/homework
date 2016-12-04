with open("file.txt", "r", encoding="utf-8") as r:
    lines = r.readlines()
    num_l = len(lines)
summ = 0
q = 0.
for line in lines:
    words = line.split()
    num_w = len(words)
    summ += num_w
q = summ / num_l
print(q)