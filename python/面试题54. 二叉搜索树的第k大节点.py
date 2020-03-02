# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            res.append(root.val)
            if len(res) == k:
                return res[-1]
            root = root.left
