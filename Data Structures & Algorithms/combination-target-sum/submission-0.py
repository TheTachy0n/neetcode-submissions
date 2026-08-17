class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        - res array
        - def backtrack wiht params (i,path,total)
        - if total == target -> append to res the copy of the path
        - if i == len(nums) or total > target -> return
        - now with nums[i] -> append it to path
        - not backtrack once again with total+nums[i] as the param
        - now pop it from path
        - after this skip nums[i] and backtrack from i+1
        - outside def let the backtrack params be (0,[],0)
        - return res
        '''
        res = []

        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if i == len(nums) or total > target:
                return

            #include nums[i]
            path.append(nums[i])
            backtrack(i,path,total + nums[i])
            path.pop()

            #skip nums[i]
            backtrack(i+1,path,total)
        
        backtrack(0,[],0)
        return res