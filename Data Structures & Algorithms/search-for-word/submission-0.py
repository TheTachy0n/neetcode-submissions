class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        - rows = len(board) cols = len(board[0])
        - define backtrack(r,c,i)->
        - if i == len(word) -> True, base case
        - if rows or columns are not in bounds -> False
        - or if the board has a letter thats not in the word -> False
        - mark some visited alphabets as marked -> '#'
        - found assess all cases
        - assign letters as temps
        - return found
        - now for each row, column if the backtrack condition is satisfied -> True
        - else False
        '''

        rows = len(board)
        cols = len(board[0])

        def backtrack(r,c,i):
            # find the entire word
            if i == len(word):
                return True
            
            #boundary conditions
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            #if the wrong Character is already visited
            if board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            # Explore 4 directions
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            #undo
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        
        return False
