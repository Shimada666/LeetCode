# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        WHITE, GRAY = 0, 1
        stack = []
        init_level = 0
        stack.append((root, WHITE, init_level))
        tmp = []
        while stack:
            node, color, level = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((node.right, WHITE, level + 1))
                    stack.append((node.left, WHITE, level + 1))
                    stack.append((node, GRAY, level))
                else:
                    if len(tmp) == level:
                        tmp.append([])
                    tmp[level].append(node.val)
        return [(sum(i))/len(i) for i in tmp]
