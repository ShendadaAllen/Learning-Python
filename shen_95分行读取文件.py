file = open("readme", mode="r+", encoding="utf-8")
read = file.readline()
read2 = file.readline()
print(read, end="")
print(read2)

file.close()
