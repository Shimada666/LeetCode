# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(nums) * len(nums[0])
        if r * c == size:
            flatten = [i for row in nums for i in row]
            return list(zip(*[iter(flatten)] * c))
        else:
            return nums


if __name__ == '__main__':
    print(Solution().matrixReshape([[4, 2],[4, 2]], 1, 4))
