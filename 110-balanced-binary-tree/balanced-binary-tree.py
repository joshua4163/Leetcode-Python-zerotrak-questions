# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]
        def balanced(root):
            if not root:
                return 0

            left = balanced(root.left)
            if balance[0] is False:
                return 0
            right = balanced(root.right)
            if abs(left - right) > 1:
                balance[0] = False
                return 0
            return 1 + max(left,right)
        balanced(root)
        return balance[0]
