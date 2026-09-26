class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1chars = [0] * 26
        window = [0] * 26

        j = 0
        # get frequency of each char in s1, window
        while j < len(s1):
            s1chars[ord(s1[j]) - ord('a')] += 1
            window[ord(s2[j]) - ord('a')] += 1
            j += 1
        if s1chars == window: # immediate match
            return True
        
        i = 0
        while j < len(s2):
            window[ord(s2[i]) - ord('a')] -= 1
            window[ord(s2[j]) - ord('a')] += 1
            if window == s1chars:
                return True
            i += 1
            j += 1
        return False
