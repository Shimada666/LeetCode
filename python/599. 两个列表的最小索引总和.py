# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {list1[i]: i for i in range(len(list1))}  # 转换hash
        map2 = {list2[i]: i for i in range(len(list2))}  # 转换hash
        inter = set(list1) & set(list2)  # 求交集
        sum_index = {i: map1[i] + map2[i] for i in inter}  # 交集成员索引求和
        return [val for val in inter if sum_index[val] == min(sum_index.values())]  # 找最少的索引和的成员


if __name__ == '__main__':
    print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                    ["KFC", "Shogun", "Burger King"]))
