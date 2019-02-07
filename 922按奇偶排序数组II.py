class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        t1 = []
        t2 = []
        for num in A:
            if num%2 == 0:
                t2.append(num)
            else:
                t1.append(num)
        res = [0 for _ in range(len(A))]
        for i in range(0,len(A),2):
            res[i] = (t2[i//2])
            res[i+1] = (t1[(i // 2)])
        return res
