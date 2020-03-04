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
    """颜色标记法"""

    # 简单版本
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    '''无需额外空间的优化版本'''

    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack, rst = [root], []
    #     while stack:
    #         i = stack.pop()
    #         if isinstance(i, TreeNode):
    #             stack.extend([i.val, i.right, i.left])
    #         elif isinstance(i, int):
    #             rst.append(i)
    #     return rst
