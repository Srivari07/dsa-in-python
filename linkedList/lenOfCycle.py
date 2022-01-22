class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def lengthCycle(self, head: ListNode) -> int:
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # Calulate the length
                temp = ListNode()
                temp = slow
                length = 0
                while temp != fast:
                    temp = temp.next
                    length += 1
                return length

        return 0
