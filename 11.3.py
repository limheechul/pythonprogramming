class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def show(self):
        print(f'({self.x},{self.y})')
    def set(self,x,y):
        self.x = x
        self.y = y
    def get(self):
        return (self.x,self.y)

class Rectangle:
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lt = Point(self.x1,self.y1)
        self.rb = Point(self.x2,self.y2)
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.lt.get()}이고 우측 하단 꼭지점이 {self.rb.get()}인 사각형입니다.', end='')
    def getWidth(self):
        return self.x2 - self.x1
    def getHeight(self):
        return self.y2 - self.y1
    def getArea(self):
        return self.getWidth() * self.getHeight()
    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) * 2
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
