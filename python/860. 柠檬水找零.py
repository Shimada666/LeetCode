# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                dic[5] += 1
            elif i == 10:
                dic[5] -= 1
                dic[10] += 1
            else:
                if dic[10] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                else:
                    dic[5] -= 3
            if dic[5] < 0:
                return False
        return True
