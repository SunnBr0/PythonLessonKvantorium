for i in range(10):
    print("Значения",i)
for i in range(2,10):
    print("Значения другого цикла",i)
for i in range(2,10,3):
    print("Значения другого иного цикла",i)
for i in range(10):
    if i ==4:
        continue
    print("Значения c continue",i)
for i in range(10):
    if i == 7:
        break
    print("Значения c break",i)

