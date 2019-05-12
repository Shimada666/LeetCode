# -*- coding: utf-8 -*-
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_item = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_item is None or self.min_item > x:
            self.min_item = x

    def pop(self) -> None:
        x = self.stack.pop()
        if not self.stack:
            self.min_item = None
        elif x == self.min_item:
            self.min_item = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_item