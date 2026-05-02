# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(root, depth):
            if not root: return depth
            depth += 1
            left = dfs(root.left, depth)
            right = dfs(root.right, depth)
            return max(left, right, left+right-2*depth)

        left = dfs(root.left, 0)
        right = dfs(root.right, 0)

        return left + right