# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for i in ops:
            if i.replace('-', '').isdigit():
                score.append(int(i))
            elif i == 'C':
                score.pop()
            elif i == 'D':
                score.append(score[-1] * 2)
            elif i == '+':
                score.append(score[-1] + score[-2])

        return sum(score)


if __name__ == '__main__':
    score = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(score))
