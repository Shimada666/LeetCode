# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' + 'b' * (n - 1) if n % 2 == 0 else 'a' * n
