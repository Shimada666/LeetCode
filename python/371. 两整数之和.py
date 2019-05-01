# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:
        n = abs(min(a, b))
        a, b = a + n, b + n
        while b != 0:
            tmp_a = a
            a = a ^ b
            b = tmp_a & b
            b <<= 1
        return a - 2 * n

        # 取巧
        # return sum([a, b])


print(Solution().getSum(43, 3))
