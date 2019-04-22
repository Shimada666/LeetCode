class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email=set()
        for i in emails:
            name,addr=i.split('@')
            name=name.split('+')[0]
            name=name.replace('.','')
            email.add(name+'@'+addr)
        return len(email)