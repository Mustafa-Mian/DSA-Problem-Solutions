class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If you can eat at a certain speed then you can eat at all higher speeds.
        # Bin search on speeds.
        lo = 1
        hi = max(piles)
        res = hi
        while lo <= hi:
            k = (lo + hi) // 2
            hours = 0
            for i in range(len(piles)):
                hours = hours + math.ceil(piles[i] / k)
            if hours <= h:
                res = k
                hi = k - 1
            else:
                lo = k + 1
        return res

                