# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        while 1:
            n_lst = list(map(int, list(str(n))))
            sum = 0
            for i in n_lst:
                sum += i ** 2
            if sum in dic:
                return False
            if sum == 1:
                return True
            dic[sum] = sum
            n = sum
