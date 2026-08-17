class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        - sort the nums
        - set res
        - define a backtrack function with start and path as params
        - append a path copy to res
        - for loop from start to len(nums)
        - if i>start and [i] == [i-1] -> continue, to skip duplicates
        - append nums[i] to path
        - backtrack from i+1
        - pop path
        - backtrack(0,[])
        - return res
        '''

        nums.sort()
        res = []

        def backtrack(start,path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0,[])
        return res