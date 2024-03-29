class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

class Rectangle(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def get_area(self):
        area = abs(self.p1.x - self.p2.x)*abs(self.p1.y - self.p2.y) 
        
        return area

    def get_perimeter(self):
        perimeter = abs(self.p1.x - self.p2.x)*2 + abs(self.p1.y - self.p2.y)*2

        return perimeter

    def is_square(self):
        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):
            return True
        else:
            return False
        

p1 = Point(1, 3)
p2 = Point(3, 1)

r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# # 출력 예시
# # 4
# # 8
# # True

# # 9
# # 12
# # True