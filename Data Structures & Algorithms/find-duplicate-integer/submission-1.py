class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        - create a slow and fast pointer
        - in a while loop if the slow and fast pointer ever get a common point
        - find slow and return it
        '''
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow