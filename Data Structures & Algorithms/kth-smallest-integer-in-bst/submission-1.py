# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''
        - dfs function with node as param
        - within define nonlocal k
        - base case
        - assign left as dfs(node.left) -> if left is not None -> return left
        - k -= 1
        - if k == 0 -> return node.val
        - return dfs(node.right)
        - finally outside the function -> return dfs(root)
        '''
        def dfs(node):
            nonlocal k

            if not node:
                return None
            
            left = dfs(node.left)
            if left is not None:
                return left
            
            k -= 1
            if k == 0:
                return node.val
            
            return dfs(node.right)
        return dfs(root)