# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        - define diameter as 0
        - define a function:
        - set a diameter variable and an edge case(not node)
        - diameter = max(diameter, left + right)
        - return 1 + max(left,right)
        - run the function wiht root as the parameter
        - return diameter
        '''

        diameter = 0
        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)
            return 1 + max(left,right)

        dfs(root)
        return diameter
