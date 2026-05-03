# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getlength(head):
            length, curr = 0, head
            while curr:
                length += 1
                curr = curr.next
            return length

        m = getlength(headA)
        n = getlength(headB)
        l1, l2 = headA, headB

        if m<n:
            m, n = n, m
            l1, l2 = headB, headA

        while m - n:
            m -= 1
            l1 = l1.next

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1