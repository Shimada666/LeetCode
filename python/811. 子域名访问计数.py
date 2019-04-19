# -*- coding: utf-8 -*-

'''
示例 1:
输入:
["9001 discuss.leetcode.com"]
输出:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
说明:
例子中仅包含一个网站域名："discuss.leetcode.com"。按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。

'''


class Solution:
    def subdomainVisits(self, cpdomains: list) -> list:
        dic = {}
        for i in cpdomains:
            lst = i.split(" ")
            domain_lst_split = lst[1].split(".")
            domain_lst = []
            for i in range(len(domain_lst_split)):
                domain = '.'.join(domain_lst_split[i:])
                domain_lst.append(domain)
            for j in domain_lst:
                if j not in dic.keys():
                    dic[j] = int(lst[0])
                else:
                    dic[j] += int(lst[0])
        lst = []
        for i in dic.keys():
            new_str = str(dic[i]) + ' ' + i
            lst.append(new_str)

        return lst


if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    print(Solution().subdomainVisits(cpdomains))
