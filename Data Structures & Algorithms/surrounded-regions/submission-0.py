class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        edgeO = deque()
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]
        for i in range(ROWS):
            for j in range(COLS):
                if onEdge(i, j, ROWS, COLS) and board[i][j] == "O":
                    board[i][j] = "T"
                    edgeO.append((i, j))
        
        # queue of "T" nodes
        while edgeO:
            i, j = edgeO.popleft()
            for k in range(4):
                ni = i + dirX[k]
                nj = j + dirY[k]
                if (ni < 0 or ni == ROWS or nj < 0 or nj == COLS):
                    continue
                if board[ni][nj] != "O":
                    continue
                board[ni][nj] = "T"
                edgeO.append((ni, nj))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

def onEdge(i, j, ROWS, COLS):
    if i == 0:
        return True
    if i == ROWS - 1:
        return True
    if j == 0:
        return True
    if j == COLS - 1:
        return True
    return False