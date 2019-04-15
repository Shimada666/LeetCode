# -*- coding: utf-8 -*-
class Solution:
    # 普通写法
    # def addDigits(self, num: int) -> int:
    #     def add(sum) -> int:
    #         new_sum = 0
    #         for i in range(len(str(sum))):
    #             new_sum += int(str(sum)[i])
    #         return new_sum
    #
    #     sum = num
    #     while (len(str(sum)) > 1):
    #         sum = add(sum)
    #
    #     return sum

    # 高端O(1)写法
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    a = 38
    print(Solution().addDigits(a))
