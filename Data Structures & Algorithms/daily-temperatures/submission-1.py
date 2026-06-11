class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                top = stack.pop()
                dist = i - top[1]
                result[top[1]] = dist
            stack.append([temperatures[i], i])
        return result
                
