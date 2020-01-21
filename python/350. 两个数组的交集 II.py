# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        nc1 = Counter(nums1)
        nc2 = Counter(nums2)
        nc = nc1 & nc2
        return list(nc.elements())



if __name__ == '__main__':
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
