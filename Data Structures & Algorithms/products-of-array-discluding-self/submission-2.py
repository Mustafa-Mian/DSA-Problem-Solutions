class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [0] * len(nums)
        after = [0] * len(nums)
        ret = [0] * len(nums)

        product = 1
        for i in range(len(nums)):
            prev[i] = product
            product *= nums[i]
        
        product = 1
        j = len(nums) - 1
        while j >= 0:
            after[j] = product
            product *= nums[j]
            j -= 1
        
        for i in range(len(nums)):
            ret[i] = prev[i] * after[i]
        
        return ret