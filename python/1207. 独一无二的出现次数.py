# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        a = [v for k, v in c.items()]
        b = set(a)
        return len(a) == len(b)


if __name__ == '__main__':
    print(Solution().uniqueOccurrences([1,2]))
