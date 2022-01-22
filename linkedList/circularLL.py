

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class CirularLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.next = self.head
        self.tail = node

    def delete(self, val):
        node = self.head
        if node == None:
            return

        if node.value == val:
            self.head = self.head.next
            self.tail.next = self.head
            return
        n = node.next
        if node != self.head:
            while True:
                node = node.next
                if n.val == val:
                    node.next = n.next
                    break

    def display(self):
        node = self.head
        if self.head != None:
            while True:
                print(f"{node.value} -> ", end=" ")
                node = node.next

                if node == self.head:
                    break
            print("HEAD")


CLL = CirularLinkedList()
CLL.insert(3)
CLL.insert(2)
CLL.insert(8)
CLL.insert(17)
CLL.delete(8)
CLL.display()
