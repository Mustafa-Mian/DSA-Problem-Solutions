class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return lookBack(len(nums)-1, nums)

def lookBack(i, nums):
    if i <= 0:
        return True
    for j in range(i-1, -1, -1):
        jumpDist = nums[j]
        dist = i - j
        if jumpDist >= dist:
            return lookBack(j, nums)
    return False