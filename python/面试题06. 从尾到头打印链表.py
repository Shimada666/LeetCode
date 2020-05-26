# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = collections.deque()
        while head:
            res.appendleft(head.val)
            head = head.next
        return list(res)
