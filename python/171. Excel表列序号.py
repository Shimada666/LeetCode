# -*- coding: utf-8 -*-
class Solution:
    def titleToNumber(self, s: str) -> int:
        cnt = 0
        sum = 0
        for i in s[::-1]:
            sum += (ord(i) - 64) * (26 ** cnt)  # A为65,所以需要减1,例如S为A时为返回结果为1
            cnt += 1
        return sum


if __name__ == '__main__':
    print(Solution().titleToNumber('AB'))
