class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        - set a res
        - define backtrack with path and used
        - if len(path) == len(nums)-> append a copy of path to res
        - for i in range till len(nums)
        - if used[i] -> continue
        - append to path and set used to true
        - now backtrack path and used
        - pop from path
        - set used to false
        - backtrack with all used values st to false initally and return res
        '''
        res = []

        def backtrack(path,used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True

                backtrack(path,used)

                path.pop()
                used[i] = False
        backtrack([],[False]*len(nums))
        return res