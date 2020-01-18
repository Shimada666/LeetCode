# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_arr = text.split(' ')
        res = []
        for i in range(len(text_arr) - 2):
            if text_arr[i] == first and text_arr[i + 1] == second:
                res.append(text_arr[i + 2])
        return res


if __name__ == '__main__':
    print(Solution().findOcurrences('alice is a good girl she is a good student a good', 'a', 'good'))
