
class Student:
    def __init__(self, name, rollno, score) -> None:
        self.name = name
        self.rollno = rollno
        self.score = score

    def greet(self):
        print('Hello ' + self.name)

    def changeName(self, newName):
        self.name = newName
        print("Name is change to " + newName)

    def __del__(self):

        print('object gets destoryed')


# s1 is a reference variable to obj, just declaring
s1 = Student('Srivari', 17, 87.99)  # object
print(s1.name)  # instance variable
print(s1.rollno)
print(s1.score)
s1.greet()
s1.changeName('Manoj')
