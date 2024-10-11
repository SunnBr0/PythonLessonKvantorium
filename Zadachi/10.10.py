# Задача по match case:

#Задача 1 : Простой калькулятор 
# Напишите калькулятор, который принимает два числа
#  и оператор (например, +, -, *, /)
#  и с помощью match...case вычисляет результат.

valueX = int(input("Первое число "))
valueY = int(input("Второе число "))
oper = input("Операция ")
match oper :
    case "+":
        print(valueX+valueY)
    case "-":
        print(valueX-valueY)
    case "*":
        print(valueX*valueY)
    case "/":
        print(valueX/valueY)

