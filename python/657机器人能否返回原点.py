class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U_count=D_count=L_count=R_count=0
        for i in moves:
            if i == 'U':
                U_count+=1
            elif i == 'D':
                D_count+=1
            elif i == 'L':
                L_count+=1
            elif i == 'R':
                R_count+=1
        if U_count == D_count and L_count == R_count:
            return True
        else:
            return False
