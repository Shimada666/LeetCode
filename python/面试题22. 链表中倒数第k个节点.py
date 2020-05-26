# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = ListNode(0)
        p.next = head
        p1 = p
        for i in range(k):
            p1 = p1.next
        while p1 != None:
            p = p.next
            p1 = p1.next
        return p
