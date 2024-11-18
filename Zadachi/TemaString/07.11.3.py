# #Замена слов
# #Напишите программу, которая заменяет
#  все вхождения одного 
# # слова другим словом в строке.
# # replace
# # Ввод:
# #1 Привет, мир
# #2 Привет
# #3 Добрый
# # Вывод:
# # Добрый, мир
string = input("Введите предложение: ")
newString = input("Введите слов из предложения: ")
replaceWord = input("Введите слово на которое хотите заменить: ")
replaceString = string.replace(newString,replaceWord)
print(replaceString)