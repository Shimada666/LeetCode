# -*- coding: utf-8 -*-

# 感觉就是考验各个语言排序算法和语言速度
class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums.sort()
        lst=[]
        for i in range(0,len(nums),2):
            lst.append(min(nums[i],nums[i+1]))
        return sum(lst)

if __name__ == '__main__':
    nums = [1, 4, 3, 2,3,4,5,2,42,34,34,23,4,34,234,25,45,435,4,6,5,547,576,3]
    print(Solution().arrayPairSum(nums))