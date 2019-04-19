class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = ''
        count = 0
        for i in s[::-1]:
            if str != '' and i == ' ':
                return count
            if i != ' ':
                count = count + 1
                str = str + i
        return count
        #return len(s.strip().split(" ")[-1])
