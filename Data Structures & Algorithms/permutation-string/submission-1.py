class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1chars = [0] * 26
        alpha = [0] * 26
        i = 0
        j = 0
        while j < len(s1):
            s1chars[ord(s1[j]) - ord('a')] += 1
            alpha[ord(s2[j]) - ord('a')] += 1
            j += 1
        if alpha == s1chars:
            return True
        while j < len(s2):
            alpha[ord(s2[i]) - ord('a')] -= 1
            alpha[ord(s2[j]) - ord('a')] += 1
            if alpha == s1chars:
                return True
            i += 1
            j += 1
        return False