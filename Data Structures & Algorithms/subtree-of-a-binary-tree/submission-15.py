# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        q1 = deque([root])
        while q1:
            node1 = q1.popleft()
            if node1 and node1.val == subRoot.val:
                if self.isSameTree(node1, subRoot):
                    return True
            if node1:
                q1.append(node1.left)
                q1.append(node1.right)

        return False
    
    def isSameTree(self, root, subroot):
        q1 = deque([root])
        q2 = deque([subroot])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
        return not q1 and not q2