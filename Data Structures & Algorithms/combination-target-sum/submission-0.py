class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        cur_comb = []
        createCombos(0, combinations, cur_comb, 0, nums, target)
        return combinations

def createCombos(i, combinations, cur_comb, cur_sum, nums, target):
    if cur_sum == target:
        combinations.append(cur_comb.copy())
        return
    if i >= len(nums) or cur_sum > target:
        return
    
    # include i
    cur_comb.append(nums[i])
    cur_sum = cur_sum + nums[i]
    createCombos(i, combinations, cur_comb, cur_sum, nums, target)

    # exclude i
    cur_comb.pop()
    cur_sum = cur_sum - nums[i]
    createCombos(i + 1, combinations, cur_comb, cur_sum, nums, target)