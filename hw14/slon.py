import re

def substitute():
    with open("art.txt","r", encoding="utf-8") as f:
        text = f.read()
    reg = r'\b(слон)((ы?)|(а(м|х)?и?)?|(у)?|(о(м|в))?|е?)\b'
    regcap = r'\b(Слон)((ы?)|(а(м|х)?и?)?|(у)?|(о(м|в)?)?|(е)?)\b'

    result = re.sub(r"́","", text)
    result = re.sub(reg, r"комар\2", result)
    result = re.sub(regcap, r"Комар\2",result)
    with open("res.txt","w", encoding="utf-8") as fw:
        fw.write(result)

substitute()