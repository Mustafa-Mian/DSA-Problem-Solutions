class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # knowing you can eat at rate k means you can eat
        # at all rates > k. Binary search on rates.

        maxRate = max(piles)
        minRate = maxRate
        l = 1
        r = maxRate

        while l <= r:
            k = (l + r) // 2
            elapsed = 0
            for pile in piles:
                hoursTaken = math.ceil(pile / k)
                elapsed += hoursTaken
            if elapsed <= h:
                # good, throw away all higher
                r = k - 1
                minRate = min(minRate, k)
            else:
                # took too long, anything smaller will
                # take too long, throw away all lower
                l = k + 1
        return minRate
            