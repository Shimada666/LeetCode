class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 2 ** (len(bin(num)) - 2) - 1 - num