# Definition for singly-linked list.

'''
https://leetcode.com/problems/palindrome-linked-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        mid = self.middleNode(head)
        headSecond = self.reverseList(mid)
        reReverseHead = headSecond

        while head != None and headSecond != None:
            if head.val != headSecond.val:
                break

            head = head.next
            headSecond = headSecond.next
        self.reverseList(reReverseHead)
        return headSecond == None or head == None

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
