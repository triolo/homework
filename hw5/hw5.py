a = input()
alist = list(a)
m = []
ind = 0
while a:
    for el in alist:
        if ind % 3 == 2:
            alist[ind] = ''
        ind += 1
    ares = ''.join(alist)
    ares = ares[::-1]
    m.append(ares)
    a = input()
    alist = list(a)
    ind = 0
for word in m:
    print(word)
