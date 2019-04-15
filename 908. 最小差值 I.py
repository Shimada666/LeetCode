# -*- coding: utf-8 -*-
class Solution:
    def smallestRangeI(self, A: list, K: int) -> int:

        min_ = max(A) - min(A)
        if min_ <= 2 * K:
            return 0
        else:
            return min_ - 2 * K


if __name__ == '__main__':
    A = [0, 10]
    K = 2
    print(Solution().smallestRangeI(A, K))
