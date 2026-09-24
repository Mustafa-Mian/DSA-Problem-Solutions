class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord('a') - ord(char)] += 1
            anagrams[tuple(chars)].append(word)
        
        ret_list = []
        for charset, group in anagrams.items():
            ret_list.append(group)
        return ret_list