class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        final_L = -1
        final_R = -1

        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                final_L = L + 1
                final_R = R + 1
                break
            elif sum > target:
                R -= 1
            else:
                L += 1
        return [final_L, final_R]
            