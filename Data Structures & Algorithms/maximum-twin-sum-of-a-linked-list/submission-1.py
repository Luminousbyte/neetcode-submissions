# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        move = head
        max_val = 0
        while move:
            value = move.val + prev.val
            move = move.next
            prev = prev.next
            max_val = max(value, max_val)
        
        return max_val
