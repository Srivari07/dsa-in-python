from typing import final, overload
import zope.interface


class Engine(zope.interface.Interface):
    price = zope.interface.Attribute('foo')

    def cost(self, price):
        price = 78000

    def start(self):
        pass

    def stop(self):
        pass

    def acc(self):
        pass


@zope.interface.implementer(Engine)
class Car:
    def cost(self, price):
        return price

    def start(self):
        print("I am of start this car")

    def stop(self):
        print("I am of stop this car")

    def acc(self):
        print("I am of acc this car")


obj = Car()

obj.start()
obj.acc()
obj.stop()
