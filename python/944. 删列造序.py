# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        cnt = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j][i] >= A[j - 1][i]:
                    continue
                else:
                    cnt += 1
                    break
        return cnt
