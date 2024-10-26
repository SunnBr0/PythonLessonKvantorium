def fibonacci(num):
    if num <=0:
        return 0
    elif num == 1:
        return 1
    else:
        predVal = fibonacci(num-1)
        nextVal = fibonacci(num -2)
        return predVal + nextVal

print(fibonacci(6))