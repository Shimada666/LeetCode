# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        a=Counter(nums)
        res=[]
        for i in a.keys():
            if a[i] == 2:
                res.append(int(i))
        return res
