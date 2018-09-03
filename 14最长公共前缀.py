class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(1, len(strs)):
            l1 = len(strs[0])
            l2 = len(strs[i])
            if l1 > l2:
                length = l2
            else:
                length = l1
            if length == 0:
                return ""
            strs[0] = strs[0][0:length]
            for j in range(length):
                if strs[0][j] != strs[i][j]:
                    strs[0] = strs[0][0:j]
                    break
        return strs[0]