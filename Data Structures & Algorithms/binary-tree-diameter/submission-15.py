# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root, res: list[int]):
            if not root:
                return 0

            left = dfs(root.left, res)
            right = dfs(root.right, res)

            temp = max(left, right) + 1
            ans = max(temp-1, left + right)

            res[0] = max(res[0], ans)

            return temp
        res = [0]
        dfs(root, res)
        return res[0]