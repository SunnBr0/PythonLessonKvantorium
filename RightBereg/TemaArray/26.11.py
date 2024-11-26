question  = {
    "Корень из 9" : "3",
    "Столица Франции":"Париж",
    "Самый неубиваемый телефон":"Nokia 3310"
}
score = 0
for quest, answer in question.items():
    userAnswer = input(f"{quest}: ")
    if answer.lower() == userAnswer.lower() :
        score += 1
        print("Правильно")
    else:
        print("Неправильно")
print(f"Кол-во очков  {score} из {len(question)}")