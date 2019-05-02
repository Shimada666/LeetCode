# -*- coding: utf-8 -*-
from typing import List

'''
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            lst = [[1], [1, 1]]
            for i in range(3, numRows + 1):
                tmp_lst = [1] * i
                last_lst = lst[-1]
                for j in range(1, i - 1):
                    tmp_lst[j] = last_lst[j - 1] + last_lst[j]
                lst.append(tmp_lst)
            return lst


print(Solution().generate(5))
