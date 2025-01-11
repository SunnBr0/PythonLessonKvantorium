class Rectangle:
    def __init__(self,height,width):
        self.__height =height
        self.__width =width 
    def RectangleS(self):
        return self.height * self.width
    def getHeight(self):
        return self.__height
    def getWidth(self):
        return self.__width
    def setWidth(self,width):
        self.__width = width
    def setHeight(self,height):
        self.__height = height
rect = Rectangle(10,20)
print(rect.getWidth(),": Width")
rect.setWidth(50)
print(rect.getWidth(),": Width")
print(rect.width)