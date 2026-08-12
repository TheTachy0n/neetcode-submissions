class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. Brute Force Approach
        - use a nested for loop, one with iterator i and one with j
        - if matrix[i][j] == target -> True
        - else -> False
        '''
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
        '''
        '''2. Binary Search
        - define rows and cols
        - initialize l and r = rows*cols-1
        - follow binary search algo with 1 small change
        - rows = mid // cols & cols = mid % cols
        - rest of the procedure is just binary search
        '''
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left<=right:
            mid = (left + right)//2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False