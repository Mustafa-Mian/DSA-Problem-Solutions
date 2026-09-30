class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {}
        dp[n] = True

        return checkBreak(0, wordDict, dp, s)

def checkBreak(i, wordDict, dp, s):
    n = len(s)
    if i in dp:
        return dp[i]
    
    for word in wordDict:
        m = len(word)
        if i + m <= n and s[i:i+m] == word:
            if checkBreak(i+m, wordDict, dp, s):
                dp[i] = True
                return True
    dp[i] = False
    return False
