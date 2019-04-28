# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def divisorGame(self, N: int) -> bool:
        # 普通做法
        # return N % 2 == 0

        # 位操作
        return N & 1 == 0
