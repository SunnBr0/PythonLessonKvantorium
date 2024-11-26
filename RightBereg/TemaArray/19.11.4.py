myList = [10,2,1,1,2,5,2,3]
arrValue = []
for item in myList :
    print(item)
    if item not in arrValue:
        arrValue.append(item)

print(myList)
print(arrValue)