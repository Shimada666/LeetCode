# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        i = 0
        while i < len(S):
            while i < len(S) and S[i].isdigit():
                i += 1
            if i == len(S): break
            if S[i].lower() == S[i]:
                res.extend([a[:i] + a[i].upper() + a[i + 1:] for a in res])
            else:
                res.extend([a[:i] + a[i].lower() + a[i + 1:] for a in res])
            i += 1
        return res
