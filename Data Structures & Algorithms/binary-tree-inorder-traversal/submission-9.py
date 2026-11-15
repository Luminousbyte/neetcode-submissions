# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while True:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            if not stack:
                break

            node = stack.pop()
            res.append(node.val)

            cur = node.right

        return res