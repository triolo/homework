import random


def syllen(word):
    vowels = ["а", "о", "у", "ы", "и", "е", "ё", "ю", "я", "э"]
    leng = 0
    for symbol in word:
        if symbol in vowels:
            leng += 1
    return leng


def punct():
    return random.choice(["...", "."])


def findlen(mass, length):
    masslen = []
    for element in mass:
        if syllen(element) == length:
            masslen.append(element)
    return masslen



def verb(gram, length=2):
    with open("verbs.txt", "r", encoding="utf-8") as vf:
        if gram == "pl":
            verb = vf.readlines()[1].split()
            verblen = findlen(verb, length)
        else:
            verb = vf.readlines()[0].split()
            verblen = findlen(verb, length)
        return random.choice(verblen)


def instrumentalis(gram, length=4):
    inslen = []
    with open("ins.txt", "r", encoding="utf-8") as insf:
        if gram == "m":
            ins = insf.readlines()[0].split()
            inslen = findlen(ins, length)
        elif gram == "f":
            ins = insf.readlines()[1].split()
            inslen = findlen(ins, length)
        elif gram == "n":
            ins = insf.readlines()[2].split()
            inslen = findlen(ins, length)
        elif gram == "pl":
            ins = insf.readlines()[3].split()
            inslen = findlen(ins, length)
    return random.choice(inslen)


def instrumentalis_mod(gram, length=3):
    ins_modlen = []
    with open("ins_mod.txt", "r", encoding="utf-8") as ins_modf:
        if gram == "m":
            ins_mod = ins_modf.readlines()[0].split()
            ins_modlen = findlen(ins_mod, length)
        elif gram == "f":
            ins_mod = ins_modf.readlines()[1].split()
            ins_modlen = findlen(ins_mod, length)
        elif gram == "n":
            ins_mod = ins_modf.readlines()[2].split()
            ins_modlen = findlen(ins_mod, length)
        elif gram == "pl":
            ins_mod = ins_modf.readlines()[3].split()
            ins_modlen = findlen(ins_mod, length)
    return random.choice(ins_modlen)


def nominative(gram, length=2):
    nomlen = []
    with open("nom.txt", "r", encoding="utf-8") as nomf:
        if gram == "m":
            nom = nomf.readlines()[0].split()
            nomlen = findlen(nom, length)
        elif gram == "f":
            nom = nomf.readlines()[1].split()
            nomlen = findlen(nom, length)
        elif gram == "n":
            nom = nomf.readlines()[2].split()
            nomlen = findlen(nom, length)
        elif gram == "pl":
            nom = nomf.readlines()[3].split()
            nomlen = findlen(nom, length)
    return random.choice(nomlen)


def nominative_mod(gram, length=3):
    nom_modlen = []
    with open("nom_mod.txt", "r", encoding="utf-8") as nom_modf:
        if gram == "m":
            nom_mod = nom_modf.readlines()[0].split()
            nom_modlen = findlen(nom_mod, length)
        elif gram == "f":
            nom_mod = nom_modf.readlines()[1].split()
            nom_modlen = findlen(nom_mod, length)
        elif gram == "n":
            nom_mod = nom_modf.readlines()[2].split()
            nom_modlen = findlen(nom_mod, length)
        elif gram == "pl":
            nom_mod = nom_modf.readlines()[3].split()
            nom_modlen = findlen(nom_mod, length)
    return random.choice(nom_modlen)


def verse1():
    gramlist = ["m", "f", "n", "pl"]
    gram = random.choice(gramlist)
    length = random.choice([2, 3])
    return verb(gram,(5-length)) + " " + nominative(gram,length)


def verse2():
    gramlist = ["m", "f", "n","pl"]
    gram = random.choice(gramlist)
    length = random.choice([2, 3, 4])
    return instrumentalis_mod(gram,(7-length)) + " " + instrumentalis(gram, length)


def verse3():
    gramlist = ["m", "f", "n", "pl"]
    gram = random.choice(gramlist)
    length = random.choice([2, 3])
    return nominative_mod(gram, (5-length)) + " " + nominative(gram, length)

print(verse1().capitalize(), verse2().capitalize()+ punct(), verse3().capitalize()+ punct(), sep="\n")

