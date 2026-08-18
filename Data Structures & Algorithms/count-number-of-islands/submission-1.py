class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        - define the number of rows and columns and set the number of islands to 0
        - define dfs with params as r and c
        - case 1 if the r and c values are out of bounds
        - case 2 in the grid if the row or column is water/already visited
        - mark that the island or water is already visited
        - explore all 4 directions around the point as r+1,r-1,c+1,c-1
        - now outside the function def -> explore each value and increments islands accordingly also implement dfs for the r and c values
        - return the islands
        '''
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Water or already visited
            if grid[r][c] != "1":
                return

            # Mark as visited
            grid[r][c] = "0"

            # Explore 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands