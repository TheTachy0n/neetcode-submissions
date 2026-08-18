"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        - base case if not node -> return None
        - create a hashmap/dict old_to_new
        - define dfs for a nore wiht params r,c
        - condition 1) if already cloned -> return the node
        - condition 2) create a clone -> set a clone variable, add it to old_to_new
        - condition 3) clone all neighbours -> for each neighbour append it to clone
        - return clone
        - finally return dfs
        '''

        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            #cond 1
            if node in old_to_new:
                return old_to_new[node]

            #cond 2
            clone = Node(node.val)
            old_to_new[node] = clone

            #cond 3
            for neighbors in node.neighbors:
                clone.neighbors.append(dfs(neighbors))
            
            return clone
        
        return dfs(node)