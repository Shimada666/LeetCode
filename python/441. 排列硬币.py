# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

from math import sqrt, floor


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor(sqrt(1 / 4 + 2 * n) - 1 / 2)
