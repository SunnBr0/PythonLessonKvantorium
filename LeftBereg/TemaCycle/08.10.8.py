import random
number = random.randint(1,1000)
print("ПОпали на игру угадай число: ")
while True:
    valueInput = int(input("Введите число: "))
    if number == valueInput:
        print("Вы молодцы ,победа")
        break
    elif  valueInput >number :
        print("Число поменьше")
    elif  valueInput <number :
        print("Число побольше")
    else:
        print("ввели некоректное число")