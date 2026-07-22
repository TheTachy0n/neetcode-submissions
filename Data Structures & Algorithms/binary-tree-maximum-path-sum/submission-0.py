# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Best path passing through this node
            maxSum = max(maxSum, node.val + left + right)

            # Return one branch to the parent
            return node.val + max(left, right)

        dfs(root)
        return maxSum