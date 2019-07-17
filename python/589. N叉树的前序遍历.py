# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst = []
        self.pretree(root, lst)
        return lst

    def pretree(self, root, lst: List[int]):
        if root is None:
            return
        lst.append(root.val)
        for child in root.children:
            return self.pretree(child, lst)
