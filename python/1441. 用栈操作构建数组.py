# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        tmp = []  # 新建数组，用于与目标数组比较
        i = 1  # 元素值
        j = 0  # 目标数组索引
        while i < n+1:
            # 判断res与目标数组是否一致
            if tmp == target:
                return res
            # 对每一个数先执行推入操作
            res.append('Push')
            tmp.append(i)
            # 若该数不存在于目标数组再推出
            if tmp[-1] != target[j]:
                res.append('Pop')
                tmp.pop()
            else:
                j += 1
            i += 1
        return res
