class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy loop instead of greedy recursion
        position = len(nums) - 1

        for j in range(len(nums)-2, -1, -1):
            jumpDist = nums[j]
            dist = position - j
            if jumpDist >= dist:
                position = j
        if position == 0:
            return True
        else:
            return False