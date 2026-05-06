# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_l, l = dummy, head
        for _ in range(left-1):
            prev_l = prev_l.next
            l = l.next

        prev = None
        for _ in range(right-left+1):
            temp = l.next
            l.next = prev
            prev = l
            l = temp
              

        prev_l.next.next = l
        prev_l.next = prev

        return dummy.next