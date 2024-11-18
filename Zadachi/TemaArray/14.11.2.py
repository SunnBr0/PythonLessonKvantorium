# 1 удаляет дубликаты 
# из списка
myList = [10,2,1,1,2,5,2,3]
arrValue = []
for itemValue in myList:
    print(itemValue)
    if itemValue not in arrValue:
        arrValue.append(itemValue)

print(myList)
print(arrValue)
