# -*- coding: utf-8 -*-
from typing import List


class Solution(object):
    def __init__(self):
        self.res = set()

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return
        self.res.add(root.val)
        self.isUnivalTree(root.left)
        self.isUnivalTree(root.right)
        return len(self.res) == 1