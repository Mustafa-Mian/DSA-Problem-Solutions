class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        if n == 0:
            return 0
        max_to_left = [0] * n
        max_to_right = [0] * n
        
        best_left = 0
        for i in range(n):
            max_to_left[i] = best_left
            if height[i] > best_left:
                best_left = height[i]
        best_right = 0
        j = len(height) - 1
        while j >= 0:
            max_to_right[j] = best_right
            if height[j] > best_right:
                best_right = height[j]
            j-=1
        
        for i in range(n):
            computed = (min(max_to_right[i], max_to_left[i]) - height[i])
            if computed > 0:
                total+=computed
        return total