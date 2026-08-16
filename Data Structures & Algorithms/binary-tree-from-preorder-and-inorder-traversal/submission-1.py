# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        - set the inorderIndex as {val:i for i, val in enumerate(inorder)}
        - set the preorderIndex as = 0
        - define a function for dfs with left and right as a parameter
        - nonlocal preorderIndex
        - base case if left>right -> return none
        - rootVal -> preorder[preorderIndex] -> increment the preorder index
        - set the root as treenode(rootVal)
        - mid is the inorderIndex[rootVal]
        - root.left = dfs(left, mid - 1)
        - root.right = df(mid+1,right)
        - return the root
        - outside the function return the dfs of index values from 0 till len(inorder) - 1
        '''
        inorderIndex = {val: i for i, val in enumerate(inorder)}
        preorderIndex = 0

        def dfs(left,right):
            nonlocal preorderIndex

            if left > right:
                return None
            
            rootVal = preorder[preorderIndex]
            preorderIndex += 1
            
            root = TreeNode(rootVal)

            mid = inorderIndex[rootVal]

            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)
            
            return root

        return dfs(0,len(inorder)-1)