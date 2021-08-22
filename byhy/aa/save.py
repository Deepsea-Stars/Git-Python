def savetofile(peoplelist, avgfee):
    with open("record.txt", "a", encoding="utf8") as f:
        recodeList = [f"{name}:{avgfee}" for name in peoplelist]
        f.write("|".join(recodeList) + "\n")
