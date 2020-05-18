# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ph = ListNode(0)
        ph.next = head
        l = ph
        r = ph
        for i in range(n+1):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return ph.next
