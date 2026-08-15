# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        - if not p and not q -> True, when p and q are not none
        - if not p or not q -> False, when p or q are not none
        - if p.val is not q.val -> False if the roots are different
        - the main part is to check id the left and right nides of the tree are the same
        - return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        '''

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))