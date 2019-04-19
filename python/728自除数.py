class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for item in range(left,right+1):
            if self.is_Self_Dividing(item):
                res.append(item)
        return res

    def is_Self_Dividing(self,item):
        str_num = str(item)
        n = len(str_num)
        for num in str_num:
            try:
                if num == '0' or item % int(num) != 0:
                    return False
            except:
                return False
        return True
