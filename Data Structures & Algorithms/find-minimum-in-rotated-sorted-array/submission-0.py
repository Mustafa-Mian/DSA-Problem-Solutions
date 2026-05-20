class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        mini = nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            mini = min(mini, nums[mid])
            if nums[lo] < nums[hi]:
                return min(mini, nums[lo])
            elif nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
        return mini
