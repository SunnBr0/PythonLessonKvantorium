class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def CircleS(self):
        r = self.height/2
        return 3.14*r*r
    def RectangleS (self):
        return self.width * self.width
    
cicrle = Rectangle(10,0)
print(cicrle.CircleS())
kvadrat = Rectangle(10,10)
print(kvadrat.RectangleS())