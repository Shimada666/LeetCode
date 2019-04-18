# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            length = len(res)
            for j in range(nums2.index(i) + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    break
            if len(res) == length:
                res.append(-1)

        return res


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))
