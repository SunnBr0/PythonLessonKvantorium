myDict = {"name":"Alice","age":25,"city":"London"}
print(myDict)
print(myDict["name"])
print(myDict["city"])
myDict["city"] = "Moscow"
print(myDict)

print("Ключи",myDict.keys())
print("Значения",myDict.values())
print("Ключ-значения",myDict.items())
for key in myDict:
    print("Key: ",key)
for value in myDict.values():
    print("value: ",value)
for key,value in myDict.items():
    print("Key-value: ",key,value)

del myDict["age"]
print(myDict)
print(myDict.get("age","ключа нет"))
print(myDict.get("name","ключа нет"))
if "name" in myDict:
    print("Ключ есть")