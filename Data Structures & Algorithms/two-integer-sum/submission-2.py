class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Goal - to check whether 2 elements in an array sum upto the target
        '''1) brute force approach
        using nested for loops to sum up the elements to check whether the sum of 2 elements is equal to the target'''
        '''n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''
        '''2) Hashmap
        - we enumerate the index and the number itself in the form i:num[i]
        - we know that the complement of a number is target - num
        - if the complement exists in num then return the mappped value of the complement, i'''
        mp = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                return [mp[complement],i]
            mp[num] = i