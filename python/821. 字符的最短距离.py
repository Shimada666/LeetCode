# -*- coding: utf-8 -*-
class Solution:
    def shortestToChar(self, S: str, C: str) -> list:
        lst_index = []
        for i in range(len(S)):
            if S[i] == C:
                lst_index.append(i)

        result = []
        for i in range(len(S)):
            result.append(min(abs(i-k) for k in lst_index))

        return result


        # 双指针
        # res = []
        # for i in range(len(S)):
        #     left, right = S[i - len(S)::-1].find(C), S[i:].find(C)
        #     if left == -1: left = 10000  # 认为10000已经足够大（字符串总长）
        #     if right == -1: right = 10000
        #     res.append(min(left, right))
        # return res


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    print(Solution().shortestToChar(S, C))
