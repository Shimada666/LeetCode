# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in str(bin(n)) or '00' in str(bin(n)))
