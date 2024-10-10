import random
randomValue=random.randint(-1000,1000)
print("Попали в игру <угадали число>")
while True:
    numInput = int(input("Ваше предположение "))
    if numInput <randomValue:
        print("Число больше вашего")
    elif numInput >randomValue:
        print("Число меньше вашего")
    else:
        print("Поздравляю вы победили!!!")
        break