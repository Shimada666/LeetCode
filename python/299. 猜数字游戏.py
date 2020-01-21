# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        sc = Counter(secret)
        gc = Counter(guess)
        t = sum([i == j for i, j in zip(secret, guess)])
        return f'{t}A{sum((sc & gc).values()) - t}B'
