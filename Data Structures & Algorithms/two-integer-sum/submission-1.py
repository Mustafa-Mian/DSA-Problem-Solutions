class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in numsMap:
                return [numsMap[need], i]
            numsMap[n] = i