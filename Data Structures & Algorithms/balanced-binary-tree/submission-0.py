# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        def dfs(node):
            if not node:
                return 0
            hleft = dfs(node.left)
            hright = dfs(node.right)
            if abs(hleft - hright) > 1:
                self.ret = False
            myheight = max(hleft, hright) + 1
            return myheight
        
        dfs(root)
        return self.ret