class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says DOG!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says CAT!")
# Создание объектов
myDog = Dog("Buddy")
myCat = Cat("Whiskers")
myDog.speak()
myCat.speak()