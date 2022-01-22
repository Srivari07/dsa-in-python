

class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.tail = None
        # self.size = 0

    def insertFirst(self, val):
        node = Node(val)
        node.next = self.head
        node.prev = None
        if self.head != None:
            self.head.prev = node
        self.head = node

    def insertLast(self, val):
        node = Node(val)
        temp = self.head

        node.next = None
        if self.head == None:
            node.prev = None
            node = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node
        node.prev = temp

    def insert(self, afterVal, val):
        nodeP = self.find(afterVal)
        if nodeP == None:
            print("Does not exists")
            return
        node = Node(val)
        node.next = nodeP.next
        nodeP.next = node

        node.prev = nodeP
        if node.next != None:
            node.next.prev = node

    def find(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return node

            node = node.next
        return None

    def deleteFirst(self):
        pass

    def deleteLast(self):
        pass

    def delete(self):
        pass

    def display(self):
        node = self.head
        last = Node(None)
        while(node != None):
            print(f"{node.value} -> ", end=" ")
            last = node
            node = node.next
        print("END")

        print("Print in reverse")
        while (last != None):
            print(f"{last.value} -> ", end=" ")
            last = last.prev
        print("START")


DLL = DoublyLinkedList()
DLL.insertFirst(3)
DLL.insertFirst(2)
DLL.insertFirst(8)
DLL.insertFirst(17)
DLL.insertLast(99)
DLL.insert(8, 65)
DLL.display()
