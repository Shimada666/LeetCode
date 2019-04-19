# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSame(left,right):
            if left == None:
                return right == None
            if right == None:
                return left == None
            if left.val != right.val:
                return False
            if left.val==right.val:
                return isSame(left.left,right.right) and isSame(left.right,right.left)
        if not root:
            return True
        return isSame(root.left,root.right)