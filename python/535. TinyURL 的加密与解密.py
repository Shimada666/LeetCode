import random

tiny_dict = dict()
graph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        str = ""
        shortstr = " http://tinyurl.com/"
        while (True):
            for i in range(0, 6):
                j = random.randint(0, 61)
                str = str + (graph[j])

            shortstr = shortstr + str

            if shortstr not in tiny_dict.keys():
                tiny_dict[shortstr] = longUrl
                return shortstr

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return tiny_dict[shortUrl]


print(Codec().encode('https://leetcode.com/problems/design-tinyurl'))
