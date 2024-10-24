def isEven (number):
    if number % 2 == 0:
        return True
    return False

def isEvenUpdate (number):
    return number % 2 == 0

print(isEven(2))
print(isEven(5))

print(isEvenUpdate(2))
print(isEvenUpdate(5))