# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = sentence.split(" ")
        n = len(searchWord)
        for i in range(len(res)):
            if res[i][:n] == searchWord:
                return i+1
        return -1
