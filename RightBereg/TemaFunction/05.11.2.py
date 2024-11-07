def factorial(num):
    if num == 0:
        return  1
    else :
        return num * factorial(num -1 )
    
for num in range(1,15):
    print(num,"! = ",factorial(num))