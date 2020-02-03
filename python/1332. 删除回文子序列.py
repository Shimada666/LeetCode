# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == '': return 0
        elif s == s[::-1]: return 1  # 如果字符串是回文，直接全部删除即可。
        else: return 2  # 如果字符串不是回文，我们最多需要删两次。