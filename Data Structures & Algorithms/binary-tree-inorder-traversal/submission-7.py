# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        # Stack stores tuples of (node, visited_status)
        stack = [(root, False)]
        
        while stack:
            curr, visited = stack.pop()
            
            if curr is None:
                continue
            
            if visited:
                # If already visited, it's time to process the Root node
                result.append(curr.val)
            else:
                # Since stack is LIFO (Last-In, First-Out), we push elements 
                # in reverse order of Inorder (Left, Root, Right):
                # 1. Push Right child
                stack.append((curr.right, False))
                # 2. Push Current node back with visited = True
                stack.append((curr, True))
                # 3. Push Left child
                stack.append((curr.left, False))
                
        return result