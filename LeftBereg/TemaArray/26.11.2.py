import random
words = ["паспорт","тумбочка","программа","стоимость","колледж"]
randomWord = random.choice(words)
listWord = list(randomWord)
random.shuffle(listWord)
joinListWord = "".join(listWord)
print("Вы попали на игру Словоместка")
print("Загаданное слово:",joinListWord)
valueWord = input("Введите ваше предположение: ").lower()
if valueWord == randomWord:
    print("Ура победа")
else:
    print("Не ура победа")
