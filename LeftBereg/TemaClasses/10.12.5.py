class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def RectangleS (self):
        return self.width * self.width
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def setWidth(self,width):
        self.width = width
    def setHeight(self,height):
        self.height = height
rect = Rectangle(10,2)
print(rect.getHeight())
rect.setHeight(200)
print(rect.getHeight())
print(rect.height)
