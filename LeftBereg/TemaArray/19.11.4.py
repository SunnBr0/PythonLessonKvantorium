my_dict = {"name": "Alice", "age": 25, "city": "London"}
# Доступ к элементу
print(my_dict["name"])  # Alice
# Добавление или изменение элемента
my_dict["age"] = 26
# Удаление элемента
del my_dict["city"]
# Итерация по ключам
for student in my_dict:
    print(student)
# Итерация по значениям
for grade in my_dict.values():
    print(grade)
# Перебор ключей, значений и пар
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Проверка наличия ключа
if "name" in my_dict:
    print("Ключ 'name' существует")