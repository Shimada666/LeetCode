# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add, mul = 0, 1
        while n > 0:
            digit = n % 10
            n //= 10
            add += digit
            mul *= digit
        return mul - add
