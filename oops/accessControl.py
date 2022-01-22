

# https: // www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/

# https: // www.geeksforgeeks.org/getter-and-setter-in-python/


class A:
    num = None
    __name = None
    arr = None

    def __init__(self, num, name, arr) -> None:
        self.num = num
        self.__name = name
        self.arr = arr

    def display(self):
        print(self.num)
        print(self.__name)
        print(self.arr)

    @property
    def get_name(self):
        print('getter is called')
        return self.__name

    def set_name(self, s):
        print('setter method is called')
        self.__name = s


obj1 = A(7, "abc", [76])
# obj1.display()


class B:
    _name = None

    def __init__(self, name) -> None:
        self._name = name

    def _display(self):
        print(self._name)

    object


class C(B):
    def __init__(self, name, rno) -> None:
        super().__init__(name)
        self.rno = rno

    def printD(self):
        self._display()
        print(self._name)
        print(self.rno)


c = C('Srivari', 17)
c.printD()
print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, C))
print(hashmap(7))
