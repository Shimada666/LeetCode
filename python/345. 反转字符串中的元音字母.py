# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = list(s)
        vowels = 'aeiouAEIOU'
        i, j = 0, len(s) - 1
        while i < j:
            while s_arr[i] not in vowels and i < j:
                i += 1
            while s_arr[j] not in vowels and i < j:
                j -= 1
            if i < j:
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
                i += 1
                j -= 1
        return ''.join(s_arr)

if __name__ == '__main__':
    print(Solution().reverseVowels('aeiou'))
