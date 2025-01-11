class Task:
    def __init__(self,description,data):
        self.description = description
        self.data = data
        self.copleted = False
    def __str__(self):
        if self.copleted:
            status = "Completed"
        else:
            status = "Pending"
        return f"{self.description} (Data :{ self.data},Status:{status})"
    def markCompleted(self):
        self.copleted = True

class TaskManager:
    def __init__(self):
        self.tasks = []
    def addTask(self,task):
        self.tasks.append(task)
    def listTasks(self):
        for taskItem in self.tasks:
            print(taskItem)
    def completedTask(self,description):
        for taskItem in self.tasks:
            if taskItem.description ==description:
                taskItem.markCompleted()
                break

taskOne = Task("Buy product","2024-12-12")
print(taskOne)
taskOne.markCompleted()
print(taskOne)
print("################")
taskTwo = Task("Убраться дома","2024-12-17")
taskThird = Task("Покормить собаку","2024-12-18")
taskFour = Task("Сделать ДЗ","2024-12-17")
tsManager = TaskManager()
tsManager.addTask(taskOne)
tsManager.addTask(taskTwo)
tsManager.addTask(taskThird)
tsManager.addTask(taskFour)
tsManager.listTasks()
tsManager.completedTask("Убраться дома")
print("################")
tsManager.listTasks()
