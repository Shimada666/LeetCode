# -*- coding: utf-8 -*-
from typing import List


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.appendleft(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    a= MyQueue()
    for i in range(3):
        a.push(i)
    print(a.queue)
