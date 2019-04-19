class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string=''.join('%s' %id for id in digits)
        intD=int(string)
        afterIntD=intD+1
        digits=list(map(int,str(afterIntD)))
        return digits
