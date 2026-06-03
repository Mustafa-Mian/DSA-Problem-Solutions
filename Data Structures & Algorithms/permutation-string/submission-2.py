class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Better solution in O(n) instead of O(26 * n)
        if len(s1) > len(s2):
            return False
        s1chars = [0] * 26
        alpha = [0] * 26
        for j in range(len(s1)):
            s1chars[ord(s1[j]) - ord('a')] += 1
            alpha[ord(s2[j]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1chars[i] == alpha[i]:
                matches += 1
        i = 0
        j = len(s1)
        while j < len(s2):
            if matches == 26:
                return True
            
            removing = ord(s2[i]) - ord('a')
            alpha[removing] -= 1
            if alpha[removing] == s1chars[removing]:
                matches += 1
            elif s1chars[removing] - 1 == alpha[removing]:
                matches -= 1
            
            adding = ord(s2[j]) - ord('a')
            alpha[adding] += 1
            if alpha[adding] == s1chars[adding]:
                matches += 1
            elif s1chars[adding] + 1 == alpha[adding]:
                matches -= 1
            i += 1
            j += 1
        return matches == 26