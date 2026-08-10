class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1. Brute Force
        inorder to get the brute force solution we can use nested for loops
        setting the product to 1 and multiplying everythign except the numebr itself
        O(n^2) time complexity
        '''
        '''
        n = len(nums)
        res = [0]*n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                prod *= nums[j]
            
            res[i] = prod
        return res
        '''
        '''
        2. Prefix and Suffix Hashing
        this uses the method where we calculate the produc of all values on the left as well as the right from the current index value
        '''
        n = len(nums)
        ans = [1]*n
        
        left = 1
        for i in range(n):
            ans[i] *= left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        
        return ans
