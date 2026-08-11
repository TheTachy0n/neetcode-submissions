class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Goal is to check the validity of the sudoku board based on the rules
        '''
        1. Brute force approach
        - using nested for loops to check each of the conditions
        - O(n^2) time complexity 3 times, space complexity is bazonkers
        - uses hashsets
        '''
        '''
        2.Using Hashmaps 
        - To optimize the process based on the rules
        - important to remember the box number algo
        - box = (r//3)*3 + (c//3)
        - if the number already exists in either row, col or box= False
        - otherwise we can just add the number to the set
        '''
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                b = (r//3)*3 + (c//3) #box

                if num in row[r] or num in col[c] or num in box[b]:
                    return False
                
                row[r].add(num)
                col[c].add(num)
                box[b].add(num)
        
        return True