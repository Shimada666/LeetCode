# -*- coding: utf-8 -*-
class Solution:
    def transpose(self, A: list) -> list:
        return list(zip(*A))



if __name__ == '__main__':
    matrix=[[1,2,3],[4,5,6]]
    print(Solution().transpose(matrix))