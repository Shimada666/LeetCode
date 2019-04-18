# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum([ord(i) for i in t])-sum([ord(i) for i in s]))
