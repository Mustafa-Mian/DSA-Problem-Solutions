class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in close_open.keys():
                stack.append(s[i])
            elif stack and close_open[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0