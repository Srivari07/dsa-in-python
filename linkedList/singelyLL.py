

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insertFirst(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

        if self.tail == None:
            self.tail = self.head
        self.size += 1

    def insertLast(self, new_value):
        if self.tail == None:
            self.insertFirst(new_value)
            return
        new_node = Node(new_value)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, new_value, index):
        if index == 0:
            self.insertFirst(new_value)
            return
        if index == self.size:
            self.insertLast(new_value)
            return
        temp = self.head
        for i in range(1, index):
            temp = temp.next
        new_node = Node(new_value, temp.next)
        temp.next = new_node
        self.size += 1

    def insertRec(self, new_value, index):
        self.head = self.__insertRec(new_value, index, self.head)

    def __insertRec(self, new_value, index, node):
        if index == 0:
            temp = Node(new_value, node)
            self.size += 1
            return temp

        node.next = self.__insertRec(new_value, index-1, node.next)
        return node

    def deleteFirst(self):
        value = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self.size -= 1
        return value

    def get(self, index):
        node = self.head
        for i in range(0, index):
            node = node.next
        return node

    def deleteLast(self):
        if self.size <= 1:
            self.deleteFirst()

        secondLast = self.get(self.size-2)
        value = self.tail.value
        self.tail = secondLast
        self.tail.next = None
        return value

    def delete(self, index):
        if index == 0:
            return self.deleteFirst()

        if index == self.size-1:
            return self.deleteLast()

        prev = self.get(index-1)
        value = prev.next.value
        prev.next = prev.next.next
        return value

    def find(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return node

            node = node.next
        return None

    # RECURSION REVERSE
    def reverse(self, node):
        if node == self.tail:
            self.head = self.tail
            return

        self.reverse(node.next)
        self.tail.next = node
        self.tail = node
        self.tail.next = None

    def reverseInplace(self):
        prev = None
        present = self.head
        next = present.next
        while present != None:
            present.next = prev
            prev = present
            present = next
            if next != None:
                next = next.next
        self.head = prev
        return prev

    def display(self):
        temp = self.head
        while(temp != None):
            print(f"{temp.value} -> ", end=" ")
            temp = temp.next
        print("END")
        print(f"Size: {self.size}")


LL = LinkedList()
LL.insertFirst(3)
LL.insertFirst(2)
LL.insertFirst(8)
LL.insertFirst(17)
LL.insertLast(99)
LL.insert(100, 3)
LL.display()
print(LL.deleteFirst())
LL.display()
print(LL.deleteLast())
LL.display()
print(LL.delete(2))
LL.display()
LL.insertRec(88, 2)
LL.display()
