# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = 1
            left = dfs(node.left)
            left += 1

            right = 1
            right = dfs(node.right)
            right += 1

            max_depth = max(left, right)
            return max_depth
        return dfs(root)