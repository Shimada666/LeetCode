# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
