class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Efficient? - using bin search
        l = 0
        r = (m * n) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_col = mid % n
            mid_row = mid // n
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

