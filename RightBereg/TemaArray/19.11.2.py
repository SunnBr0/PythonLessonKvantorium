myList = [1,2,3,"Slovo",True,1.2]
myList[1]= 100
print(myList)
print(type(myList))
listNumber = [-1,3,-100,5,2]
listNumber.append(1000)
listNumber.remove(-100)
listNumber.insert(3,25)
listNumber.pop(3)
listNumber.extend([-10,2])
listNumber.sort()
listNumber.sort(reverse=True)
listNumber.clear()
print(listNumber)