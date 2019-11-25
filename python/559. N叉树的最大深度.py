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
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if root.children is None:
            return 1
        depth = 1
        for child in root.children:
            tempDepth = self.maxDepth(child) + 1
            if tempDepth > depth:
                depth = tempDepth
        return depth
