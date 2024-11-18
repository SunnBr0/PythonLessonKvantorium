# #Палиндром
# #Напишите программу, 
# # которая проверяет,
# #  является ли строка палиндромом
# #  (читается одинаково с начала и с конца).
# # топот ,анна, алла
string = input("Введите слово: ")
reversString = string[::-1]
if string.upper() == reversString.upper():
    print("Слово палиндром")
else:
    print("Слово не палиндром")






# string = input("Введите слово: ")
# replaceString = string[::-1]
# if replaceString.upper() == string.upper():
#     print("Слово палиндром")
# else:
#     print("Слово не палиндром")

