class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        waterAmount = 0

        maxBefore = 0
        largestBefore = [0] * n
        for i in range(n):
            largestBefore[i] = maxBefore
            maxBefore = max(height[i], maxBefore)
        
        maxAfter = 0
        largestAfter = [0] * n
        for i in range(n-1, -1, -1):
            largestAfter[i] = maxAfter
            maxAfter = max(height[i], maxAfter)

        for i in range(n):
            computed = min(largestBefore[i], largestAfter[i]) - height[i]
            waterAmount += computed if computed > 0 else 0
        return waterAmount