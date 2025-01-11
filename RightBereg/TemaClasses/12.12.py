class Rectangle:
    def __init__(self,height,width):
        self.height =height
        self.width =width 
    def RectangleS(self):
        return self.height * self.width
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def setWidth(self,width):
        self.width = width
    def setHeight(self,height):
        self.height = height
rect = Rectangle(10,20)
print(rect.getWidth(),": Width")
rect.setWidth(50)
print(rect.getWidth(),": Width")
print(rect.width)