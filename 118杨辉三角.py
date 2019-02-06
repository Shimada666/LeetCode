class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(numRows):#每循环一次出现一行
            temp=[1]*(i+1)#初始化为1
            print(temp)
            res.append(temp)
            for j in range(1,i):#列
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
a=Solution()
print(a.generate(3))