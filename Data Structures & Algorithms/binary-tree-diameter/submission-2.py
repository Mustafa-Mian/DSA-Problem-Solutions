# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def heightCalc(node):
            if not node:
                return 0
            lheight = heightCalc(node.left)
            rheight = heightCalc(node.right)
            mydiameter = lheight + rheight
            self.diameter = max(self.diameter, mydiameter)

            return 1 + max(lheight, rheight)
        
        heightCalc(root)
        return self.diameter
