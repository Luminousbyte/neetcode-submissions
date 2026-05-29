"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            c_node = Node(node.val)
            hashmap[node] = c_node

            for nei in node.neighbors:
                c_node.neighbors.append(dfs(nei))
            return c_node

        return dfs(node) if node else None