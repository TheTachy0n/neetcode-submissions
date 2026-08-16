# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        - define a function to have the node and maxval as parameters
        - within in, define a base base
        - we can define a good condition as 1 if node.val >= maxval
        - maxval is the maximum of maxval and node.val
        - return (good + dfs(node.left, maxval) + dfs(node.right,maxval))
        - finally return the function with the root and root.val as the params
        '''
        def dfs(node, maxval):
            if not node:
                return 0
            
            good = 1 if node.val >= maxval else 0

            maxval = max(maxval, node.val)

            return (good + dfs(node.left,maxval) + dfs(node.right,maxval))
        return dfs(root, root.val)
