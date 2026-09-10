class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        # get frequencies
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        # make array of size maxFreq
        # fill slots with nums
        # go backwards on that array and grab k elems
        maxFreq = max(list(frequencies.values()))
        arr = [[] for _ in range(maxFreq + 1)]
        for num, count in frequencies.items():
            arr[count].append(num)

        i = len(arr) - 1
        ret = []
        while i >= 0:
            for num in arr[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
            i -= 1
        
        return ret

