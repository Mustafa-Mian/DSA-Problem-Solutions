class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion
        def recurseStairs(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2
            else:
                return recurseStairs(i-1) + recurseStairs(i-2)
        return recurseStairs(n)