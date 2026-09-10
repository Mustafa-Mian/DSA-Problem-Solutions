class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islandCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islandCount += 1
                    bfs(grid, islandCount, r, c)
        
        return islandCount

def bfs(grid, count, r, c):
    ROWS = len(grid)
    COLS = len(grid[0])
    directionX = [0, 1, 0, -1]
    directionY = [-1, 0, 1, 0]

    queue = deque()
    queue.append((r, c))
    # grid[r][c] = "0"

    while queue:
        cur_row, cur_col = queue.popleft()

        # check out of bounds
        if cur_row < 0 or cur_col < 0 or cur_row == ROWS or cur_col == COLS:
            continue
        
        if grid[cur_row][cur_col] == "1":
            grid[cur_row][cur_col] = "0"
            for i in range(len(directionX)):
                queue.append((cur_row + directionX[i], cur_col + directionY[i]))
