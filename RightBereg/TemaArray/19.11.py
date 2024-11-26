ColorArray = ["Red","Orange","Yellow","Green"]
for item in range(len(ColorArray)):
    print(f"элемент {item} значение {ColorArray[item]}")

for value in ColorArray:
    print(f"значение {value}")

listNumber = [1,2,3,4,5]
sum = 0
for value in range(len(listNumber)):
    sum += listNumber[value]
print(sum)