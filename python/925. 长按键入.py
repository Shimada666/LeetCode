# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        for j in range(len(typed)):
            if name[left] == typed[j]:
                left += 1
            if left == len(name):
                return True
        return False
