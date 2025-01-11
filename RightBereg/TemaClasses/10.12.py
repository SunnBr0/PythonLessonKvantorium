class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog = Dog("Alex",10)
print(dog.name)
print(dog.age)
labrador = Dog("Rex",15)
print(labrador.name)
print(labrador.age)
dog.name = "Ralf"
dog.age = 11
labrador.name = "Pockemon"
labrador.age = 1
print(f"Имя {dog.name} возраст {dog.age}")
print(f"Имя {labrador.name} возраст {labrador.age}")