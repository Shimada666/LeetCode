# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i, j in zip(s, t):
            if i in hashmap and j != hashmap[i]:
                return False
            if i not in hashmap and j in hashmap.values():
                return False
            hashmap[i] = j
        return True
