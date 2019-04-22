class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max=-1
        index=0
        for i in range(len(A)):
            if A[i]>max:
                max=A[i]
                index=i
        return index
