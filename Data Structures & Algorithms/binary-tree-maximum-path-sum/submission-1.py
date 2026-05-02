# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.best = float("-inf")

        def all_downward_sums(node):
            if not node:
                return []

            left_sums = all_downward_sums(node.left)
            right_sums = all_downward_sums(node.right)

            down_sums = [node.val]
            for s in left_sums:
                down_sums.append(node.val + s)
            for s in right_sums:
                down_sums.append(node.val + s)

            self.best = max(self.best, max(down_sums))

            if left_sums and right_sums:
                for ls in left_sums:
                    for rs in right_sums:
                        self.best = max(self.best, ls + node.val + rs)

            return down_sums

        def traverse_and_compute(node):
            if not node:
                return

            all_downward_sums(node)

            traverse_and_compute(node.left)
            traverse_and_compute(node.right)

        traverse_and_compute(root)
        return self.best