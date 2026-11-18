# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def height(node):
            if node is None:
                return 0

            if node in memo:
                return memo[node]

            left = height(node.left)
            right = height(node.right)

            memo[node] = 1 + max(left, right)

            return memo[node]

        def find_diameter(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            current = left + right

            left_diameter = find_diameter(node.left)
            right_diameter = find_diameter(node.right)

            return max(current, left_diameter, right_diameter)

        return find_diameter(root)