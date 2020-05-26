# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def sortString(self, s: str) -> str:
        chars = collections.Counter(s)
        ans = []
        signal = 0
        while chars:
            group = list(chars)
            group.sort(reverse=signal)
            ans.extend(group)
            chars -= collections.Counter(group)
            signal = 1 - signal
        return ''.join(ans)
