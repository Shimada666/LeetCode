# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return N ^ int('1' * len(bin(N)[2:]), 2)
