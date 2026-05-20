class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        best_width = 0
        best_len = 0

        while L < R:
            width = abs(L-R)
            length = min(heights[L], heights[R])
            area = width * length
            if area > (best_width * best_len):
                best_width = width
                best_len = length
            else:
                if length == heights[L]:
                    L+=1
                elif length == heights[R]:
                    R-=1
        return best_width * best_len
