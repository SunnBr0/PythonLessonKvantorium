for i in range(10):
    print("значение",i)
for i in range(5,10):
    print("новые значения",i)
for i in range(1,10,2):
    print("более новые значения",i)
for item in range(8):
    if item == 5:
        continue
    print("Значения continue",item)
for item in range(8):
    if item == 3:
        break
    print("Значения с break",item)