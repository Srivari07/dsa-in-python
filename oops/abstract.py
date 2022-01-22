# https://www.geeksforgeeks.org/abstract-classes-in-python/

# An abstract method is a method that has a declaration but does not have an implementation.

# abc = Abstract Base Classes

from abc import abstractmethod, ABC


class Shapes(ABC):
    @abstractmethod
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


# shape = Shapes()
circle = Circle()
triangle = Triangle()
square = Square()

# shape.area()
circle.area()
triangle.area()
square.area()
