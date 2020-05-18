# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                count += 1
        return count
