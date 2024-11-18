#1  Ввод списка чисел
# Попросите пользователя 
# ввести размер массива(list) ,
# потом несколько чисел 
#  и сохраните их в списке. 
# Выведите список на экран.
arrValue = []
height = int(input("Введите размер: "))
for i in range(height):
    numberList = int(input("значение: "))
    arrValue.append(numberList)
print(arrValue)