class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst1 = []
        lst2 = []
        for i in A:
            if i % 2 == 0:
                lst1.append(i)
            else:
                lst2.append(i)
        return lst1 + lst2
