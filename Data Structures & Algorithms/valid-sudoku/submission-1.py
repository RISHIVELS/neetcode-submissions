from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        square_hash = [defaultdict(int) for _ in range(9)]
        
        for i in range(9):
            row_hash = defaultdict(int)
            column_hash = defaultdict(int)
            for j in range(9):
                current_row_value = board[i][j]
                current_column_value = board[j][i]
                if current_row_value.isnumeric():
                    if current_row_value in row_hash : 
                        return False 
                    else : 
                        row_hash[current_row_value] = 1
                if current_column_value.isnumeric(): 
                    if current_column_value in column_hash: 
                        return False 
                    else : 
                        column_hash[current_column_value] = 1
                if board[i][j].isnumeric(): 
                    if board[i][j] in square_hash[(i//3)*3 + (j//3)]:
                        return False 
                    else : 
                        square_hash[(i//3)*3 + (j//3)][board[i][j]] = 1
        return True