# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=[i.lower() for i in licensePlate if i.isalpha()]
        words=sorted(words,key = lambda i:len(i))
        for i in words:
            tmp=[s for s in i]
            flag=0
            for s in l:
                if l.count(s)>tmp.count(s):
                    flag=1
                    break
            if flag==0:
                return i