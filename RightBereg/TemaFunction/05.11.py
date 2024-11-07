def factorial(number):
    result = 1
    for item in range (1,number+1):
        result *=item
    return result

for num in range(1,15):
    print(num,"! = ",factorial(num))