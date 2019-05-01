# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper()==word or word[1:].lower()==word[1:]