# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        j = len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        res.append(i)
        return res
