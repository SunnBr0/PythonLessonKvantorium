class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def speak(self):
        print(f"{self.name} Гав Гав!!!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Мяу Мяу!!!")

myDog = Dog("Rex")
myCat = Cat("Kuzi")
myDog.speak()
myCat.speak()