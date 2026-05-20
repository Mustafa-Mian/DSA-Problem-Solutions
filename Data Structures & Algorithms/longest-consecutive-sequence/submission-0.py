class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = set()
        longest_length = 0
        current_length = 0
        for i in range(len(nums)):
            seen_nums.add(nums[i])
        for i in range(len(nums)):
            if nums[i]-1 not in seen_nums:
                current_length = 1
                while (nums[i] + current_length) in seen_nums:
                    current_length+=1
                longest_length = max(current_length, longest_length)
                
        return longest_length

