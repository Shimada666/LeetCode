# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 != 0 and i % 5 != 0:
                res.append(str(i))
            elif i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append('Buzz')
        return res