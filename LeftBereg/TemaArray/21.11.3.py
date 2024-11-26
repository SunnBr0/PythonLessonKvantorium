questions = {
    "Какая столица России?" : "Москва",
    "Как переводится apple на русском" : "Яблоко",
    "чему равно 2+2":"4"
}
score = 0
for quest , answer in questions.items():
    userAnswer = input(f"{quest} ")
    if userAnswer.lower() == answer.lower():
        print("Правильно")
        score +=1
    else:
        print(f"Неправильно! Правильный ответ:{answer}")
print(f"Ваш итоговый счёт: {score}/{len(questions)}")
