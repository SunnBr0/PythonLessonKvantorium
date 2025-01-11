class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def woof(self):
        print(f"меня зовут { self.name} !!")
    # геттер
    def getAge(self):
        return self.age
    
shpits = Dog("Lapochka",10)
shpits.woof()
print(shpits.getAge())
