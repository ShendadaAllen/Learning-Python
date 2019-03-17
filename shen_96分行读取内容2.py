file = open("readme", mode="r+", encoding="utf-8")
while True:
    read = file.readline()
    if not read:
        break
    else:
        rd = input("确认读下一行回车")
        if rd == "q" or rd == "Q":
            break
        else:
            print(read, end="")
file.close()
