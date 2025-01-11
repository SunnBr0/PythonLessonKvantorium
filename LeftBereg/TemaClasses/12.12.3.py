class Task:
    def __init__ (self,description,data):
        self.description = description
        self.data = data
        self.completed = False
    def __str__(self):
        if self.completed :
            status = "Completed"
        else:
            status = "Pending"
        return f"{self.description} (Data: {self.data},Status: {status})"
    def markCompleted(self):
        self.completed =True

class TaskManager:
    def __init__(self):
        self.tasks = []
    def addTask(self,task):
        self.tasks.append(task)
    def listTasks(self):
        for taskItem in self.tasks:
            print(taskItem)
    def completedTask (self,description):
        for taskItem in self.tasks:
            if taskItem.description == description:
                taskItem.markCompleted()
                break

taskOne = Task("Buy product","2024-12-12")
print(taskOne)
taskOne.markCompleted()
print(taskOne)
print("###################")
taskTwo = Task("ExamMath","2024-12-13")
taskThird = Task("Новый Год","2024-12-31")
taskFour = Task("Домашние ДЗ","2024-12-14")
tsManager = TaskManager()
tsManager.addTask(taskOne)
tsManager.addTask(taskTwo)
tsManager.addTask(taskThird)
tsManager.addTask(taskFour)
tsManager.listTasks()
tsManager.completedTask("Новый Год")
print("###################")
tsManager.listTasks()