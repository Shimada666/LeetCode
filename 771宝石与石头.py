class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        lst = []
        for i in J:
            if i not in lst:
                lst.append(i)
        count = 0
        for j in S:
            if j in lst:
                count += 1
        return count
