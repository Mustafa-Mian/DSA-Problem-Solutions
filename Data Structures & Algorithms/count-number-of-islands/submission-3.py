class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j, grid)
        return count

def bfs(i, j, grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    queue = deque([])
    queue.append((i, j))
    grid[i][j] = "0"

    directionX = [0, 1, 0, -1]
    directionY = [-1, 0, 1, 0]
    while queue:
        r, c = queue.popleft()

        for k in range(len(directionX)):
            nr = r + directionX[k]
            nc = c + directionY[k]

            if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                continue
            if grid[nr][nc] == "0":
                continue
            queue.append((nr, nc))
            grid[nr][nc] = "0"
    return