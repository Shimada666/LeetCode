# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(L, R + 1):
            if bin(i).count('1') in prime:
                res += 1
        return res



if __name__ == '__main__':
    Solution().countPrimeSetBits(6,10)