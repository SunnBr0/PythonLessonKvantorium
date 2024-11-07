string = "Hello, World!!!"
part = string[2:8]
print("part",part)
arrFruits = "banana,apple,cherry"
partFruit = arrFruits.split(",")
print("partFruit", partFruit)

countChar = arrFruits.count("a")
print("countChar", countChar)
lowerString = string.lower()
print("lowerString", lowerString)
print(arrFruits.upper())

print(arrFruits.replace("banana","minon"))
print("//".join(partFruit))