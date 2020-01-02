# -*- coding: utf-8 -*-
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        # 定义了两个节点a和b，只要a和b不等就继续遍历
        while a != b:
            # 这步很关键，请对照动态图配合理解，
            # 当a的下一个为空时，就a就从b链表头开始遍历
            a = a.next if a else headB
            # 同理，b也是类似的
            b = b.next if b else headA
        return a
