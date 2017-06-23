import re
import os

def open_file():
    with open("text.xml", "r", encoding="utf-8") as f:
        text = f.readlines()
    return text


def open_file_oneline():
    with open("text.xml", "r", encoding="utf-8") as f:
        oneline = f.read()
    return oneline

def write_into_txt(dict):
    res = ""
    with open("task1.txt", "w", encoding="utf-8") as file:
        for i in dict.keys():
            res += "\n" + i.strip() + "\t" + str(dict[i])
        file.write(res)
def write_header():
    string = u"FILENAME" + "," + "AUTHOR" + "," + "TEXT CREATED"
    with open("task2.csv", "w", encoding="cp866") as file:
        file.write(string)

def append_to_csv(file,auth,date):
    string = "\n" + file + "," + auth + "," + date
    with open("task2.csv", "a", encoding="cp866") as file:
        file.write(string)
def separate_sentences(oneline):
    sentlist = []
    for i in re.finditer(r"<se>(.*?)</se>", oneline):
        sentlist.append(i.group(1))
    return sentlist


def task1():
    namenum ={}
    for root, dirs, files in os.walk("news"):
        for f in files:
            with open(os.path.join(root, f), "r", encoding="cp866") as f1:
                lines = f1.readlines()
                wordnum = 0
                for line in lines:
                    if "<w" in line:
                        wordnum += 1
            namenum[f] = wordnum
    write_into_txt(namenum)


def task2():
    author = ""
    date = ""
    write_header()
    for root, dirs, files in os.walk("news"):
        for f in files:
            with open(os.path.join(root, f), "r", encoding="cp866") as f1:
                oneline = f1.read()
                for i in re.finditer(r"<meta content=\"(.*?)\" name=\"author\"></meta>", oneline):
                    author = i.group(1)
                for j in re.finditer(r"<meta content=\"(.*?)\" name=\"created\"></meta>", oneline):
                    date = j.group(1)
                append_to_csv(f, author, date)

def task3():
    massent = []
    mass = []
    reg =r"<w><ana lex=\"(.*?)\" gr=\"A(.*?)=(.*?)gen(.*?)\"></ana>(.*?)</w>\n<w><ana lex=\"(.*?)\" gr=\"S(.*?)=(.*?)gen(.*?)\"></ana>(.*?)</w>"

    for root, dirs, files in os.walk("news"):
        for f in files:
            with open(os.path.join(root, f), "r", encoding="cp866") as f1:
                oneline = f1.read()
                sentlist = separate_sentences(oneline)
                for sent in sentlist:
                    for i in re.finditer(reg, sent):
                        bigram = i.group(5) + " " +i.group(10)
                        mass.append(bigram)
                        massent.append(sent)
    with open("task3.txt", "w", encoding="cp866") as wf:
        for el in mass:
                wf.write("\n"+el)

def main():
    task1()
    task2()
    task3()

main()