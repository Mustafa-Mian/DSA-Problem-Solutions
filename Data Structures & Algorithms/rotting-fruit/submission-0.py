class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        freshCount = 0

        for i in range(ROWS):
            for j in range(COLS):
                val = grid[i][j]
                if val == 1:
                    freshCount += 1
                if val == 2:
                    queue.append((i, j))
        dirX = [1, 0, -1, 0]
        dirY = [0, -1, 0, 1]
        mins = 0
        while freshCount > 0 and queue:
            length = len(queue)
            for x in range(length):
                # queue only contains rotten, so we can
                # assume anything popped is rotten.
                i, j = queue.popleft()
                for k in range(4):
                    ni = i + dirX[k]
                    nj = j + dirY[k]
                    if not (ni<0 or ni==ROWS or nj<0 or nj==COLS) and grid[ni][nj] == 1:
                        freshCount -= 1
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
            mins += 1
        if freshCount == 0:
            return mins
        else:
            return -1
