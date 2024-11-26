vowels = {"а","е",
          "ё","и","о",
          "у","ы","э","ю","я"}

letter = input("Введите букву")
if letter.lower() in vowels:
    print("Буква гласная")
else:
    print("Согласная буква")