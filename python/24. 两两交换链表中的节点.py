# -*- coding: utf-8 -*-讷讷不语
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        s = ListNode(0)
        s.next = head

        prev = s
        while head and head.next:
            n1 = head
            n2 = head.next

            prev.next, n1.next, n2.next = n2, n2.next, n1

            prev = n1
            head = n1.next
        return s.next
