
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

import copy


class Human:
    def __init__(self, name, age, arr) -> None:
        self.name = name
        self.age = age
        self.arr = arr

    def display(self):
        print(self.name)
        print(self.age)
        print(self.arr)


srivari = Human("srivari", 20, [3, 4, 5, 6, 7, 8, 2])
# twin = copy.copy(srivari) # shallow copy
twin = copy.deepcopy(srivari)  # deep copy
twin.arr[0] = 100
srivari.display()

twin.display()
