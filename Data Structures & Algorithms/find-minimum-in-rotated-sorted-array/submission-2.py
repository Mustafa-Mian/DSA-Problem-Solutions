class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            mini = min(mini, val)
            if nums[l] < nums[r]:
                # we are in sorted portion of array,
                # return start of subarray or mini
                return min(mini, nums[l])
            if val >= nums[r]:
                # we are not in sorted portion of array
                l = mid + 1
            elif val < nums[r]:
                # this portion of array is locally sorted
                r = mid - 1
        return mini

