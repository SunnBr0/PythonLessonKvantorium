# y = x*1.5 +10
#функция
def yFunc(x):
    y = x*1.5+10
    return y 
# процедура 
def printFunc(valueX,valueY):
    print(f"x = {valueX} ")
    print(f"y = {valueY}")
    print(f"{valueY} = {valueX}*1.5 +10")

xValue = int(input("Напишите х: "))
print(yFunc(xValue))
printFunc(xValue,yFunc(xValue))