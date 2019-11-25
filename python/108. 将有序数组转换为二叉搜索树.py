# -*- coding: utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            tn = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            tn.left = self.sortedArrayToBST(nums1)
            nums2 = nums[mid + 1:len(nums)]
            tn.right = self.sortedArrayToBST(nums2)
        return tn

if __name__ == '__main__':
    print(Solution().sortedArrayToBST([-3,0,5]).left.val)