# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        s_arr = sorted(arr)
        min_arr = [s_arr[i + 1] - s_arr[i] for i in range(len(s_arr) - 1)]
        res = []
        min_ = min(min_arr)
        for i in range(len(min_arr)):
            if min_arr[i] == min_:
                res.append([s_arr[i], s_arr[i + 1]])
        return res
