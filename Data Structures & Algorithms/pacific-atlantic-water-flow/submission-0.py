class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        - set the rows and the columns
        - let pacific and altantic be sets
        - define dfs with parameters r,c,visited
        - if r,c in visited -> return
        - add r,c to visited
        - set a list of tuples as the directions
        - for loop with dr and dc -> all conditions
        - dfs(nr,nc,visited)
        - condition for pacific ocean and atlantic ocean
        - cells reachable from both oceans
        '''

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if (nr, nc) in visited:
                    continue

                # Reverse flow:
                # We can move to a cell only if its height
                # is >= the current cell's height.
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # Pacific Ocean: top row + left column
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic Ocean: bottom row + right column
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Cells reachable from BOTH oceans
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result