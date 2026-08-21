class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # simple O(n) space
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        return -1