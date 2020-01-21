# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class MyHashSet:
    N = 20011

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[] for _ in range(self.N)]

    def add(self, key: int) -> None:
        t = key % self.N
        for item in self.hash[t]:
            if item == key:
                return
        else:
            self.hash[t].append(key)

    def remove(self, key: int) -> None:
        t = key % self.N
        for item in self.hash[t]:
            if item == key:
                self.hash[t].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        t = key % self.N
        for item in self.hash[t]:
            if item == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
