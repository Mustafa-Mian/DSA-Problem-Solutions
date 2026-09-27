# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def heightCalc(root):
            if not root:
                return 0
            lheight = heightCalc(root.left)
            rheight = heightCalc(root.right)
            myDiameter = lheight + rheight
            self.maxD = max(myDiameter, self.maxD)
            return 1 + max(lheight, rheight)
        heightCalc(root)
        return self.maxD