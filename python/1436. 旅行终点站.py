# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        end_city = set()
        begin_city = set()
        for path in paths:
            end_city.add(path[1])
            begin_city.add(path[0])
        return (end_city - begin_city).pop()
