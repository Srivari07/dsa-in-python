
''' 
https://www.geeksforgeeks.org/python-interface-module/
'''

import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('foo')

    def method1(self, x, y, z):
        pass

    def method2(self):
        pass


@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x**2

    def method2(self):
        return "foo"


obj = MyClass()

# ask an interface whether it
# is implemented by a class:
print(MyInterface.implementedBy(MyClass))

# MyClass does not provide
# MyInterface but implements it:
print(MyInterface.providedBy(MyClass))

# ask whether an interface
# is provided by an object:
print(MyInterface.providedBy(obj))

# ask what interfaces are
# implemented by a class:
print(list(zope.interface.implementedBy(MyClass)))

# ask what interfaces are
# provided by an object:
print(list(zope.interface.providedBy(obj)))

# class does not provide interface
print(list(zope.interface.providedBy(MyClass)))
