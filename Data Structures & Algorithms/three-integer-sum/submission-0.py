class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            seen_vals = {}
            target = -1 * num
            while L < R:
                if L == i:
                    L+=1
                    continue
                if R == i:
                    R-=1
                    continue
                sum = nums[L] + nums[R]
                if sum > target:
                    R-=1
                elif sum < target:
                    L+=1
                else:
                    triplets.append([nums[L], nums[R], num])
                    L+=1
                    R-=1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        return triplets

