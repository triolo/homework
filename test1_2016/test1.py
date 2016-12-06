m = []
s_ipm = 0
user_input = ' '
f = 0
with open("freq.txt", "r", encoding="utf-8") as r:
    lines = r.readlines()
    for line in lines:
        m = line.split(" | ")
        if m[1] == "союз":
            print(line.strip(), end="\n")

    print("\n\n")

    for line in lines:
        m = line.split(" | ")
        g = m[1].split()
        if ("ед" in g) & ("жен" in g):
            print(m[0].strip(), end=", ")
            ipm = float(m[2].strip())
            s_ipm += ipm
    print("\nСумма ipm:", s_ipm)

inp_l = []
out_l = []
while user_input:
    user_input = input("Вводите слова, затем нажмите Ввод еще раз: ")
    inp_l.append(user_input)

for line in lines:
    m = line.split(" | ")
    for i in range(len(inp_l)-1):
        if inp_l[i] == m[0].strip():
            for k in range(len(inp_l)-1):
                out_l.append(' ')

            out_l[i] = line.strip()
            f = 1
            break

for j in range(len(out_l)):
    if out_l[j] == ' ':
        out_l[j] = "Слово не найдено!"
print(out_l, sep='\n')








