class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        if x > 0:
            str_x = str(x)
            str_x = str_x[::-1]
            x = int(str_x)
            if -2147483648 < x < 2147483647:
                return x
            else: return 0

        elif x < 0:
            x = -x
            str_x = str(x)
            str_x = str_x[::-1]
            x = int(str_x)
            if -2147483648 < x < 2147483647:
                x = -x
                return x
            else: return 0
