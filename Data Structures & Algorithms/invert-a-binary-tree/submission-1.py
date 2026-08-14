# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        - recursion based
        - check whether a root exists, if no -> return None
        - assign variable left as inverttree of root left
        - assign variable right as inverttree of root.right
        - now simply equate root.left, root.right with left and right
        - finally return root
        '''

        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root