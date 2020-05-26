# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if root:
            ans, f = [], lambda r: r and (f(r.left) or ans.append(r) or f(r.right))
            f(root)
            for i, r in enumerate(ans[1:]):
                ans[i].left = None
                ans[i].right = r
            ans[-1].left = None
            return ans[0]
