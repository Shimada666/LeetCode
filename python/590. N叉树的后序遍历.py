# -*- coding: utf-8 -*-
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root) -> List[int]:
        lst = []
        self.posttree(root, lst)
        return lst

    def posttree(self, root, lst: List[int]):
        if root is None:
            return

        for child in root.children:
            self.posttree(child, lst)
        lst.append(root.val)
