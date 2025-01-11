class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

class Quiz:
    def __init__(self,filename):
        self.questions = self.loadQuestions(filename)
        self.score = 0

    def loadQuestions(self,filename):
        question = []
        with open(filename,"r",encoding="utf-8") as file:
            lines = file.readlines()
            for item in range(0,len(lines),2):
                questionText = lines[item].strip()
                answerTest = lines[item+1].strip()
                question.append(Question(questionText,answerTest))
        return question
    
    def start(self):
        for questionItem in  self.questions:
            userAnswer = input(f"{questionItem}: ")
            if userAnswer.lower() == questionItem.answer.lower():
                print("Правильно")
                self.score += 1
            else:
                print(f" Неверно ответ такой : {questionItem.answer}")
        print(f"Квиз закончен ,Ваши очки {self.score} / {len(self.questions)}")

example = Question("Сколько 2+2","4")
quiz = Quiz("questions.txt")
quiz.start()
