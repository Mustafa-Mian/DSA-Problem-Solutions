class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlpha(s[l].lower()):
                l += 1
            while r > l and not isAlpha(s[r].lower()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

def isAlpha(char):
    if ord(char) >= ord("a") and ord(char) <= ord("z"):
        return True
    if ord(char) >= ord("0") and ord(char) <= ord("9"):
        return True
    return False