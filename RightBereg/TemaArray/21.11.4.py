myDict = {"name": "Alice",
          "age":25,
          "city":"London"}
print(myDict)
print(myDict["name"])
print(myDict["city"])
myDict["city"] = "Moscow"
print(myDict.values())
print(myDict.keys())
print(myDict.items())

for key in myDict:
    print("key",key)
for value in myDict.values():
    print("value",value)
for key,value in myDict.items():
    print("key,value",key,value)

del myDict["age"]
print(myDict)

print(myDict.get("age","ключа нет"))
print(myDict.get("name","ключа нет"))

if "name" in myDict:
    print("Есть ключ")