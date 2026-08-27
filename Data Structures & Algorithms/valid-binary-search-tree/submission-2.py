# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    valid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, max_so_far, min_so_far):
            if not node:
                return True
            if node.val >= max_so_far:
                return False
            if node.val <= min_so_far:
                return False
            else:
                return dfs(node.left, node.val, min_so_far) and dfs(node.right, max_so_far, node.val)
        
        return dfs(root, float('inf'), float('-inf'))