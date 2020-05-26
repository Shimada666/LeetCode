# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        left, right = 0, 1
        while right < len(s):
            if s[right] != s[left]:
                res = max(right - left, res)  # 这样写最后还要更新
                left = right
            right += 1
        return max(right - left, res)  # 必须更新
