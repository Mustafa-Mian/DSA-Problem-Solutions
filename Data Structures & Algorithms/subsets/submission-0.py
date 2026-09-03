class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        cur_set = []
        includeValues(0, subsets, cur_set, nums)
        return subsets

def includeValues(i, subsets, cur_set, nums):
    # reached the end of decision making, save list
    if i >= len(nums):
        subsets.append(cur_set.copy())
        return
    
    # include i in cur_set
    cur_set.append(nums[i])
    includeValues(i + 1, subsets, cur_set, nums)

    # exclude i from cur_set
    cur_set.pop()
    includeValues(i + 1, subsets, cur_set, nums)