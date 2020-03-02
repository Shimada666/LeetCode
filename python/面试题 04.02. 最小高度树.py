# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        half_len = length // 2
        root = TreeNode(nums[half_len])
        root.left = self.sortedArrayToBST(nums[:half_len])
        root.right = self.sortedArrayToBST(nums[half_len+1:])
        return root