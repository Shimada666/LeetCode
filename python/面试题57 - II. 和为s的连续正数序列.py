# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1

        return res
