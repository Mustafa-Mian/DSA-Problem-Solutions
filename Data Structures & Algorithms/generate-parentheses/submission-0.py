class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(s, openC, closeC):
            if openC == closeC == n:
                output.append(s)
                return
            if openC < n:
                backtrack(s + "(", openC + 1, closeC)
            if closeC < openC:
                backtrack(s + ")", openC, closeC + 1)
        
        backtrack("", 0, 0)
        return output