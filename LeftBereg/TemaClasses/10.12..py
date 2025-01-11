class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
dog = Dog("Alex",10)
print(dog.name,dog.age)
labrador = Dog("Rex",15)
print(labrador.age,labrador.name)
dog.name = "Ralf"
dog.age = 1
labrador.name = "Pockemon"
labrador.age = 5
print(f"Имя {dog.name} возраст {dog.age}")
print(f"Имя {labrador.name} возраст {labrador.age}")