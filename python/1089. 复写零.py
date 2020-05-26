# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while i < l:
            if arr[i] == 0:
                #遇到0复制插入，同时删除尾数
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
