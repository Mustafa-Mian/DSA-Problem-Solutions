class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_word = int(s[i:j]) # from i (first digit) to j (posn of #)
            word = s[j + 1 : j + 1 + length_word]
            result.append(word)
            i = j + 1 + length_word
        
        return result
        
