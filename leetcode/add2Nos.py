from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        while l1 != None or l2 != None or carry == 1:
            summ = 0
            if l1 != None:
                summ = summ+l1.val
                l1 = l1.next
            if l2 != None:
                summ = summ+l2.val
                l2 = l2.next
            summ = summ+carry
            carry = summ//10
            node = ListNode(summ % 10)
            curr.next = node
            curr = curr.next

        return dummy.next

ss=Solution()
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(ss.addTwoNumbers(l1,l2))