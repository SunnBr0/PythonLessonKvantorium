vowels = {"а","е","у","о","ы","ё","и","ю","я","э"}
letter = input("Введите букву: ")
if letter.lower() in vowels:
    print("Гласная буква")
else:
    print("Согласная буква")