# -*- coding: utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 递归
        # if root is None:
        #     return None
        # if val == root.val:
        #     return root
        # if val < root.val:
        #     return self.searchBST(root.left, val)
        # if val > root.val:
        #     return self.searchBST(root.right, val)

        # 迭代
        while root:
            if root.val == val:
                return root
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
        return None
