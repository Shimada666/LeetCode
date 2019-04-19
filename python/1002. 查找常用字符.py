# -*- coding: utf-8 -*-
class Solution(object):
    def commonChars(self, A: list):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        letter_list = set(A[0])
        for i in A:
            letter_list = letter_list & set(i)

        dic = {}

        for i in letter_list:
            min_ = 99999
            for j in A:
                cnt = 0
                for k in j:
                    if k == i:
                        cnt += 1
                if cnt < min_:
                    min_ = cnt
            dic[i] = min_

        lst = []
        for i in dic.keys():
            for j in range(dic[i]):
                lst.append(i)

        return lst


if __name__ == '__main__':
    print(Solution().commonChars(["bella", "label", "roller"]))
