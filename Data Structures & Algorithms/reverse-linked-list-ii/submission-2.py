# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_l, l = dummy, head
        l_x, r_y = (left - 1), (right - left + 1)
        while l_x:
            l = l.next
            prev_l = prev_l.next
            l_x -= 1

        prev = None
        while r_y:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
            r_y -= 1

        prev_l.next.next = l
        prev_l.next = prev

        return dummy.next