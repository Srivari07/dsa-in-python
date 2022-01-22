
# https://docs.python.org/3/library/typing.html

# Generic programming is a style of computer programming in which algorithms are written in terms of types to-be-specified-later that are then instantiated when needed for specific types provided as parameters.
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.push(7)
stack.pop()
stack.push('x')  # type error
stack.push(True)  # type error
print(stack.items)
