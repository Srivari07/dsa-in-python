

'''
https://leetcode.com/problems/reorder-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return

        mid = self.middleNode(head)
        hf = head
        hs = self.reverseList(mid)
        while hf != None and hs != None:
            temp = hf.next
            hf.next = hs
            hf.next = temp

            temp = hs.next
            hs.next = hf
            hs = temp

            if hf != None:
                hf.next = None

    def reverseList(self, head):
        prev = None
        present = head
        next = present.next
        while present != None:
            present.next = prev
            prev = present
            present = next
            if next != None:
                next = next.next
        head = prev
        return prev

    def middleNode(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
