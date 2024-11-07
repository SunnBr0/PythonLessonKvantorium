string ="    Hello, World    "
print(string.strip())
name = "Alice"
age = 22
formatString = "Name {},age {}".format(name,age)
print(formatString)
print(name[::-1])
print(len(name))
strHi = "Hello, World"
subString = "Hello"
if subString in strHi:
    print("Подстрока найдена")
else:
    print("Подстрока не найдена")