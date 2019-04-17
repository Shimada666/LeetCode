# -*- coding: utf-8 -*-
from typing import List


class Solution:
    # 普通做法
    # def singleNumber(self, nums: List[int]) -> int:
    #     dic={}
    #     for i in nums:
    #         if i not in dic.keys():
    #             dic[i]=1
    #         else:
    #             dic[i]+=1
    #     for k,v in dic.items():
    #         if v==1:
    #             return k

    # 异或操作
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res^=i
        return res


if __name__ == '__main__':
    print(Solution().singleNumber([4,1,2,1,2]))