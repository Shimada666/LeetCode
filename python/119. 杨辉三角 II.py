# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        if rowIndex == 0:
            return []
        elif rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
        else:
            lst = [[1], [1, 1]]
            for i in range(3, rowIndex + 1):
                tmp_lst = [1] * i
                last_lst = lst[-1]
                for j in range(1, i - 1):
                    tmp_lst[j] = last_lst[j - 1] + last_lst[j]
                lst.append(tmp_lst)
            return lst[-1]


print(Solution().getRow(3))
