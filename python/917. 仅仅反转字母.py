# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) < 2:
            return S
        i, j = 0, len(S) - 1  # -1 则是下标
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S = ''.join([S[:i], S[j], S[i + 1:j], S[i], S[j + 1:]])
                i, j = i + 1, j - 1
            elif S[i].isalpha() and not S[j].isalpha():
                j = j - 1
            elif not S[i].isalpha() and S[j].isalpha():
                i = i + 1
            elif not S[i].isalpha() and not S[j].isalpha():
                i, j = i + 1, j - 1
        return S

if __name__ == '__main__':
    a='a-b-c-d'
    print(Solution().reverseOnlyLetters(a))