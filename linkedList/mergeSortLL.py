

"""
https://leetcode.com/problems/sort-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        mid = self.middleNode(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):

        dummyHead = curHead = ListNode()
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curHead.next = l1
                curHead = curHead.next
                l1 = l1.next
            else:
                curHead.next = l2
                curHead = curHead.next
                l2 = l2.next

        if l1 != None:
            curHead.next = l1
        if l2 != None:
            curHead.next = l2
        return dummyHead.next

    def middleNode(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
