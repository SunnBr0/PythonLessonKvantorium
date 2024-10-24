def square(number):
    return number * number
print("Результат ",square(10))

def maxOfTwo(num1,num2):
    if num1>num2 :
        return num1
    else :
        return num2
numOne = 10
numTwo=-14
strNum = f"Числа {numOne} и {numTwo}"
maxValue = maxOfTwo(numOne,numTwo)
print(strNum,"из них больше всего",maxValue)