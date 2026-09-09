class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if checkBoard(board, word, 0, i, j, set()):
                    return True
        return False

def checkBoard(board, word, pos, row, col, visited):
    if pos == len(word):
        return True
    if row < 0 or row == len(board):
        return False
    if col < 0 or col == len(board[0]):
        return False

    cur_val = board[row][col]

    if (row, col) in visited:
        return False

    if cur_val == word[pos]:
        visited.add((row, col))
        present = (
            checkBoard(board, word, pos + 1, row, col - 1, visited) 
            or checkBoard(board, word, pos + 1, row, col + 1, visited) 
            or checkBoard(board, word, pos + 1, row - 1, col, visited) 
            or checkBoard(board, word, pos + 1, row + 1, col, visited)
            )
        visited.remove((row, col))
        if present:
            return True
    else:
        return False

def nextPos(board, row, col):
    if col == len(board[0]) - 1:
        return (row + 1, 0)
    else:
        return (row, col + 1)