class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = (ROWS * COLS) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_col = mid % COLS
            mid_row = mid // COLS
            val = matrix[mid_row][mid_col]

            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = l + 1
        return False