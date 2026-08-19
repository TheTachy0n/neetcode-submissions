from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        - Import a queue
        - row and cols, and start a queue
        - add all treasures to the queue
        - directions - list of tuples
        - while the queue ->r,c = pop the queue
        - for dr and dc in directions -> compute nr and nc
        - check boundaries
        - only visit the unvisited land
        - change the distance as 1 + current distance
        - append nr and nc to the queue
        '''
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Put ALL treasure cells into the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Only visit unvisited land
                if grid[nr][nc] != 2147483647:
                    continue

                # Distance = current distance + 1
                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr, nc))