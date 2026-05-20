class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in s_letters:
                s_letters[letter] = 0;
            else:
                s_letters[letter]+=1
        for letter in t:
            if letter not in t_letters:
                t_letters[letter] = 0;
            else:
                t_letters[letter]+=1
        if s_letters == t_letters:
            return True
        return False