# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        while len(A) >= 3:
            f = A[0]
            s = A[1]
            t = A[2]
            if f - s < t:
                return f + s + t
            else:
                A.pop(0)
        return 0