class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    @staticmethod
    def iAmDog():
        print("Класс собака!!!")
    @classmethod
    def iAmDogTwo(cls):
        print("Класс собака###")
    def woof(self):
        print("Рык!!")

Dog.iAmDog()
Dog.iAmDogTwo()
doggy = Dog("Baby",3)
doggy.woof()