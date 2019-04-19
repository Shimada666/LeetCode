# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        s = (A + ' ' + B).split(' ')
        return [i for i in set(s) if s.count(i) == 1]
