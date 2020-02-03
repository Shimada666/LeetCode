# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get_ch(num):
            return chr(int(num) + 96)

        ans, i = '', len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans += get_ch(s[i - 2: i])
                i -= 3
            else:
                ans += get_ch(s[i])
                i -= 1
        return ans[:: -1]
