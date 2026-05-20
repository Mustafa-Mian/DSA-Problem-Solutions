class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = [0] * n
        after = [0] * n
        products = [0] * n

        prev[0] = 1
        after[n - 1] = 1
        for i in range(1, n):
            prev[i] = prev[i-1] * nums[i-1]
        j = n - 2
        while j > -1:
            after[j] = after[j+1] * nums[j+1]
            j -= 1
        for i in range(n):
            products[i] = prev[i] * after[i]
            
        return products