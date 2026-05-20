class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        lst = list(frequencies.items())
        lst = sorted(lst, reverse=True, key=lambda x: x[1])
        ret_lst = []
        for i in range(k):
            ret_lst.append(lst[i][0])
        return ret_lst
        