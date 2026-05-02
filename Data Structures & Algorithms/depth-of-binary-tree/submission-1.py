# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            print(f"Returned 0")
            return 0

        print(root.val)

        depth = 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        print(f"depth:", depth)
        return depth