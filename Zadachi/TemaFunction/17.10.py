# Задача написать функцию для расчёта  площадей 
# А) Квадрат,
# где a - сторона квадрата S = a * a 
# def sKvadrat (a)
# Б) Круг ,
# где r - радиус круга, 
# S = r^2 * Pi = r * r * Pi 
# def sCircle( r)
# В) Треугольник , 
# где a ,b ,c - стороны треугольника ,
# def sTreg(a,b,c)
#  по формуле Герона 
# S = sqrt(p*(p-a)*(p-b)*(p-c)) ,
#  p = (a + b + c) / 2
import math
def sKvadrat(a):
    return a * a
print("Площадь квадрата: ",sKvadrat(4))
def sCircle (r):
    # S = r*r*pi
    pi = math.pi
    return r*r*pi
print("Площадь круга: ",sKvadrat(2))
def sTriangle(a,b,c):
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S
print("Площадь треугольника: ",sTriangle(2,2,2))

    # S = sqrt(p*(p-a)*(p-b)*(p-c)) ,
    # p = (a + b + c) / 2
















# import math
# def sKvadrat(a):
#     return a*a
# storona = 10
# print(sKvadrat(storona))
# def sCircle(r):
#     return r*r*math.pi
# print (sCircle(storona))
# def sTrig (a,b,c):
#     p = (a+b+c)/2
#     S = math.sqrt((p*(p-a)*(p-b)*(p-c)))
#     return S
# print(sTrig(storona,storona,storona))