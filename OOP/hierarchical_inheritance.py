class Shape:
    def display(self):
        print("This is a Shape")


class Circle(Shape):
    def area(self, radius):
        print("Area of Circle:", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self, length, breadth):
        print("Area of Rectangle:", length * breadth)


class Triangle(Shape):
    def area(self, base, height):
        print("Area of Triangle:", 0.5 * base * height)


c = Circle()
r = Rectangle()
t = Triangle()

c.display()
c.area(5)

r.display()
r.area(10, 5)

t.display()
t.area(6, 4)
