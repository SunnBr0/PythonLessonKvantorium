string  = "Hello, World"
sunString = string[0:5]
print("sunString",sunString)
arrFruits = "banana,apple,cherry"
itemFruit = arrFruits.split(",")
print("itemFruit",itemFruit)
newString = arrFruits.replace("banana","миньон")
print("newString",newString)

countStr = arrFruits.count("a")
print("countStr",countStr)
print(arrFruits.upper())
print(string.lower())
print("//".join(itemFruit))