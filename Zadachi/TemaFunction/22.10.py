#Задача 1: Нахождение максимального из трёх чисел
#Условие:
#Напишите функцию max_of_three(a, b, c), 
# которая принимает три числа и возвращает наибольшее 
# из них.\
def maxOfThree(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b < c:
        return c
    else:
        return b
print(maxOfThree(2,3,4))
print(maxOfThree(5,3,4))
print(maxOfThree(25,30,-4))
print(maxOfThree(-25,-30,-4))






# # def max_of_three(a,b,c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     elif b > c:
#         return b
#     else:
#         return c 

# numOne = 10
# numTwo = 50
# numTri = -300
# print(max_of_three(numOne,numTwo,numTri))