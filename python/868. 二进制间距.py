# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def binaryGap(self, N: int) -> int:
        res = str(bin(N))[2:].split('1')[1:-1]  # 从第一个到倒数第二个,如10000则可判定无
        max_ = -1
        for i in res:
            if len(i) > max_:
                max_ = len(i)
        return max_ + 1


if __name__ == '__main__':
    print(Solution().binaryGap(32))
