def factorial(num):
    result = 1
    for iter in range(1,num+1):
        result*=iter
    return result
for iter in range(1,10):
    res = factorial(iter)
    print(iter,"!=",res)

