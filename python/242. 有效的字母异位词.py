# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        for i in s:
            if i not in s_dic:
                s_dic[i] = 1
            else:
                s_dic[i] += 1
        for i in t:
            if i not in t_dic:
                t_dic[i] = 1
            else:
                t_dic[i] += 1
        return s_dic == t_dic

        # 解法2
        # from collections import Counter
        # return Counter(s) == Counter(t)

        # 解法3
        # return sorted(s) == sorted(t)

print(Solution().isAnagram('ab','ba'))