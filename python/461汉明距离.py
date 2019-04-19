class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #异或，统计结果1出现次数
        return bin(x ^ y).count('1')
