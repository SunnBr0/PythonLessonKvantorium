def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)
num = 5
print(f"число {num}")
print(f"факториал {factorial(num)}")