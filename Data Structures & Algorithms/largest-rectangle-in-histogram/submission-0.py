class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stores indices
        maxArea = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            maxArea = max(maxArea, h * width)

        return maxArea