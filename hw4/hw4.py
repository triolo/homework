a = input()
i = 0
for i in range(0, len(a)):
    if (i % 2 != 0) and (a[i] != 'а') and (a[i] != 'к'):
        print(a[i])
    else: continue
    
