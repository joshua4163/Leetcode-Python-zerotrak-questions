# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:  # if t is None
            return True
        if not s:  # if s is None
            return False
        if self.isSameTree(s, t):  # check if trees are identical
            return True
        # check subtrees
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:  # both are None
            return True
        if not s or not t:  # one is None, the other is not
            return False
        if s.val != t.val:  # values don't match
            return False
        # recursively check left and right subtrees
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
