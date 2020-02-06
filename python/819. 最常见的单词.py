# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        from collections import Counter
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banned:
                ans, best = word, count[word]

        return ans
