class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res=[i*i for i in A]
        res.sort()
        return res