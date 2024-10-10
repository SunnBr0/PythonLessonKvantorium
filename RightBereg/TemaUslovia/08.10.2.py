operation = input("операция")
valueX = 10
valueY= 3
match operation:
    case "+":
        print(valueX+valueY)
    case "-":
        print(valueX-valueY)
    case _:
        print("Не понятно")