import re
def openfile():
    with open("F.xml","r", encoding="utf-8") as f:
        lines = f.readlines()
    l = len(lines)
    with open("result.txt","w",encoding="utf-8") as fr:
        fr.write(str(l))
    return lines

def dict():
    d = {}
    k = []
    w = []
    ch = []
    lines = openfile()
    for line in lines:
        m = re.search(r'<w lemma="(?:.*)" type="(.*)">(.*)<',line)
        if m:
            k.append(m.group(1))
    for i in range(len(k)):
        h = 0
        for line in lines:
            m = re.search(r'<w lemma="(?:.*)" type="(.*)">(.*)<', line)
            if m:
                if m.group(1) == k[i]:
                    h = h + 1
        ch.append(h)
    for i in range(len(k)):
        d[k[i]] = ch[i]
    with open("keys.txt","w", encoding="utf-8") as fd:
        for key in d:
            fd.write(key + "\n")

def third():
    r = []
    lines = openfile()
    for line in lines:
        m = re.search(r'<w lemma="(?:.*)" type="(l.{1}f.*)">(.*)<', line)
        if m:
          r.append(m.group(1))
    with open("adj.txt", "w", encoding="utf-8") as fa:
        for i in range(len(r)):
            s = 0
            for j in range(len(r)):
                if r[i] == r[j]:
                    s = s + 1
            fa.write(r[i]+" "+str(s)+"\n")
def main():
    openfile()
    dict()
    third()
    
main()