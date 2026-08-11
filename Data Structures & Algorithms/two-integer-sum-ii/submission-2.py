class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Goal is to return the two numbers in the list that add up to the target
        '''
        we are given that the array is in non decreasing order
        Two Pointer Method
        - set an l and r pointer
        - while the l<r
        - define the target as the sum fo the num[l] and num[r]
        - since it is in non decreasing order, if the sum is greater than the target -> decrement r
        - else if the sum is less than the target -> increment l
        return num[l],num[r]
        '''
        l = 0
        r = len(numbers) - 1
        while l<r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1,r+1]
            if summ > target:
                r -= 1
            else:
                l += 1
        