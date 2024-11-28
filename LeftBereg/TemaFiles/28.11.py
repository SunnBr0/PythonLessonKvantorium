file = open("./text.txt","r",encoding="utf-8")
for item in file:
    print(item)
file.close()