# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        temp = head
        while n>0:
            temp = temp.next
            # print(temp.val)
            n -= 1
            # print(n)
        while temp:
            curr = curr.next
            temp = temp.next

        rem = curr.next
        curr.next = curr.next.next
        rem.next = None

        return dummy.next