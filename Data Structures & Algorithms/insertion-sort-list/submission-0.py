# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        lst.sort()

        curr = head
        for i in lst:
            curr.val = i
            curr = curr.next
        return head