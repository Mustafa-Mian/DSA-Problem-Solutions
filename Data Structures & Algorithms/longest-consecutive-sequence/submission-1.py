class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        seq_len = 0
        max_len = 0

        for num in nums:
            seen.add(num)

        for num in nums:
            if (num - 1) in seen:
                continue
            else:
                seq_len = 1
                while (num + seq_len) in seen:
                    seq_len += 1
            max_len = max(max_len, seq_len)
        
        return max_len