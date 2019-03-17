file = open("readme", "r", encoding="utf-8")
file_write = open("readme_复件", "w", encoding="utf-8")
while True:
    text = file.readline()
    if not text:
        break
    file_write.write(text)


file.close()
file_write.close()
