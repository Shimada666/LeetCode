# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        try:
            min_column = min([ops[i][0] for i in range(len(ops))])
            min_row = min([ops[i][1] for i in range(len(ops))])
        except:
            return m*n
        return min_column*min_row


print(Solution().maxCount(3,3,[]))