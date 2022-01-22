class Box:

    def __init__(self, l, h, w) -> None:
        self.l = l
        self.h = h
        self.w = w

    def display(self):
        print("print the box ")
        print(self.l)
        print(self.h)
        print(self.w)

# single inheritance


class BoxWeight(Box):
    def __init__(self, l, h, w, weight) -> None:
        super().__init__(l, h, w)
        self.weight = weight

    def display(self):
        print("print the box with weight ")
        print(self.l)
        print(self.h)
        print(self.w)
        print(self.weight)

# multilevel inhertance


class BoxVolume(BoxWeight):
    def __init__(self, l, h, w, weight, volume) -> None:
        super().__init__(l, h, w, weight)
        self.volume = volume

    def display(self):
        print("Box with volume")
        self.volume = self.l * self.h * self.w
        print(self.volume)

# muliple inhertance


class BoxPrice(BoxVolume, BoxWeight):
    def price(self, cost):
        self.cost = cost

    def display(self):
        print("price")
        self.cost = self.weight+self.volume
        print(self.cost)

# herarical inheritance
# boxweight and boxcolor => box class inherit


class BoxColor(Box):
    def color(self):
        print("Blue Colour")


# hybrid ineritance
# comination of single and muliple inheritance
obj1 = Box(10, 20, 30)
obj1.display()

obj2 = BoxWeight(10, 20, 30, 50)
obj2.display()

obj3 = BoxVolume(10, 20, 30, 50, 0)
obj3.display()

obj4 = BoxPrice(10, 20, 30, 50, 6000)
obj4.display()
