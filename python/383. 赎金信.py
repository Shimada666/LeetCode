# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        a = Counter(ransomNote)
        b = Counter(magazine)
        for key in a.keys():
            if a[key] > b[key] or key not in b:
                return False
        return True
