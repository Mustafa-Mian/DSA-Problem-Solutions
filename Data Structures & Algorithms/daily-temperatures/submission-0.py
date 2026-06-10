class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temp:
                    result[i] = count
                    break
                count += 1
        return result