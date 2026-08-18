class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        - similar to number of islands problem
        - max area variable to 0
        - initial area = 1, increment the area every dfs
        - finally max area is the max of Max_area or dfs(r,c)
        '''

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0:
                return 0

            # Mark as visited
            grid[r][c] = 0

            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area