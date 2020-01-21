# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[] for _ in range(20011)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        t = key % 20011
        for item in self.hash[t]:
            if item[0] == key:
                item[1] = value
                return
        self.hash[t].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        t = key % 20011
        for item in self.hash[t]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        t = key % 20011
        delete = []
        for item in self.hash[t]:
            if item[0] == key:
                delete = item
        if delete:
            self.hash[t].remove(delete)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
