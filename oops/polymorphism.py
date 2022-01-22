
from typing import final, overload


class Shapes:
    # final is use to prevent overridding
    # @final
    def area(self):
        print('I am a shape')


class Circle(Shapes):
    def area(self):
        print('I am a circle')


class Triangle(Shapes):
    def area(self):
        print('I am a triange')


class Square(Shapes):
    def area(self):
        print('I am a square')

# here, methodoverriding is achived


shape = Shapes()
circle = Circle()
triangle = Triangle()
square = Square()

shape.area()
circle.area()
triangle.area()
square.area()
