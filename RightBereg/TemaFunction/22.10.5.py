def checkNumber(number):
    if number > 0:
        return "Положительное"
    elif number < 0 :
        return "Отрицательное"
    else:
        return "Равняется нулю"
print(checkNumber(10))
print(checkNumber(-10))
print(checkNumber(0))