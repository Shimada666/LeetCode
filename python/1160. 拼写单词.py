from typing import *
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(list(chars))
        res = []
        flag = True
        for word in words:
            tmp_counter = Counter(list(word))
            for key in tmp_counter.keys():
                if tmp_counter[key] > counter[key]:
                    flag = False
                    break
            if flag:
                res.append(word)
            else:
                flag = True
        return sum([len(i) for i in res])


if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(Solution().countCharacters(words,chars))