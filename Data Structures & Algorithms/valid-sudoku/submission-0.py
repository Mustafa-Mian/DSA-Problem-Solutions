class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = self.check_rows(board)
        valid_cols = self.check_cols(board)
        valid_squares = self.check_squares(board)
        return (valid_rows and valid_cols and valid_squares)
    
    def check_rows(self, board):
        for row in board:
            numbers_seen = {}
            for i in range(0, len(row)):
                if row[i] != "." and row[i] in numbers_seen:
                    return False
                numbers_seen[row[i]] = i
        return True
    
    def check_cols(self, board):
        for i in range(0, 9):
            numbers_seen = {}
            for j in range(0, 9):
                cell_value = board[j][i]
                if cell_value != "." and cell_value in numbers_seen:
                    return False
                numbers_seen[cell_value] = j
        return True
    
    def check_squares(self, board):
        numbers_seen = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                my_square = (r // 3, c // 3)
                value_at = board[r][c]
                if value_at in numbers_seen[my_square] and value_at != ".":
                    return False
                numbers_seen[my_square].add(value_at)
        return True
        
