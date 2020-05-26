# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ret, queries_count, words_count = [], [], []
        words_count = [word.count(min(word)) for word in words]
        for query in queries:
            c = query.count(min(query))
            # 在 words_count 里数一下有多少是比 c 大的
            ret.append(len([x for x in words_count if c < x]))
        return ret
