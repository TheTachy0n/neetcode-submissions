from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()      # stores indices
        res = []
        left = 0

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            # Remove indices outside the window
            if q[0] < left:
                q.popleft()

            # Window has reached size k
            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1

        return res