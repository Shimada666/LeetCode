# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for num in res:
                res = res + [[i] + num]
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
