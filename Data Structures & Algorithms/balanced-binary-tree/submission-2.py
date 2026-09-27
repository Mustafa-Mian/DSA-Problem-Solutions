# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        def checkBalance(root):
            if not root:
                return 0
            lheight = checkBalance(root.left)
            rheight = checkBalance(root.right)
            if abs(lheight - rheight) > 1:
                self.ret = False
            return max(lheight, rheight) + 1
        
        checkBalance(root)
        return self.ret