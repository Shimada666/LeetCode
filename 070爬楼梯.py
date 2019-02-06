class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        way = [0, 1, 2]
        for i in range(3, n + 1):
            way.append(way[i - 1] + way[i - 2])
        return way[n]

a=Solution()
print(a.climbStairs(15))