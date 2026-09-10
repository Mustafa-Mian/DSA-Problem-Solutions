class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = searchArea(grid, r, c, visited)
                    maxArea = max(maxArea, area)
        
        return maxArea

def searchArea(grid, r, c, visited):
    ROWS = len(grid)
    COLS = len(grid[0])
    queue = deque()
    queue.append((r, c))
    area = 0
    directionX = [1, 0, -1, 0]
    directionY = [0, -1, 0, 1]

    while queue:
        cur_row, cur_col = queue.popleft()

        if cur_row < 0 or cur_col < 0 or cur_row == ROWS or cur_col == COLS:
            continue
        
        if visited[cur_row][cur_col]:
            continue

        val = grid[cur_row][cur_col]
        if val == 0:
            continue
        if val == 1:
            visited[cur_row][cur_col] = True
            area += 1
            for i in range(len(directionX)):
                offsetX = cur_row + directionX[i]
                offsetY = cur_col + directionY[i]
                queue.append((offsetX, offsetY))
    return area
