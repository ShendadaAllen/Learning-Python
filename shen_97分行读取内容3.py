file = open("readme", mode="r+", encoding="utf-8")
while True:
    read = file.readline()
    if not read:
        break

    print(read, end="")
file.close()

