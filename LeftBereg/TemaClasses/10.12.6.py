# инкапсуляция 1 принцип
class Rectangle:
    def __init__(self,height,width):
        self.__height = height
        self.__width = width
    def RectangleS (self):
        return self.__width * self.__width
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setWidth(self,width):
        self.__width = width
    def setHeight(self,height):
        self.__height = height
rect = Rectangle(10,2)
print(rect.getHeight())
rect.setHeight(200)
print(rect.getHeight())
# print(rect.height)

