# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        s = set()
        s.add(head.val)
        while cur.next:
            if cur.next.val in s:
                cur.next = cur.next.next
            else:
                s.add(cur.next.val)
                cur = cur.next
        return head
