# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.number = n

        def rec(head):
            if not head:
                return None

            head.next = rec(head.next)
            self.number -= 1

            if self.number == 0:
                return head.next
            return head

        return rec(head)