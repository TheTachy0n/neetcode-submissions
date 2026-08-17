class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
             
        '''
        - create a res
        - define a backtrack function with i and path as parameters
        - if i is equal tot he length of nums
        - append a copy of the path ro the res and return
        - now append the num in index i to path
        - and backtrack(i+1,path)
        - now pop the last element in path
        - and again backtrack(i+1,path)
        - now outside the function definition backtrack(0,[])
        - return res
        '''
        res = []  
        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            # Include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)

            # Undo
            path.pop()

            # Don't include nums[i]
            backtrack(i + 1, path)

        backtrack(0, [])

        return res