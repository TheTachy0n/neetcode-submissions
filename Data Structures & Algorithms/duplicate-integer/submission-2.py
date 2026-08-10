class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''goal- check if a duplicate exists in the list nums
        - we have to use sets
        - we know that sets don't contain repeated values
        - brute force solution would be to simply check whether each element of the array is equal to the next but the time complexity would be O(n)
        - Better solution would be appending each element to a set and checking if its already there in the hashset ''' 

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
