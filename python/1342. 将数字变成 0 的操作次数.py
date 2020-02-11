# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            num = num / 2 if num % 2 == 0 else num - 1
            res += 1
        return res
