arrList = []
nValue =int(input("Размер массива: "))
for _ in range(nValue):
    newValue = int(input("Введите число: "))
    arrList.append(newValue)
print(arrList)
countValue = arrList.count(5)
print("countValue",countValue)
arrList.reverse()
print(arrList)