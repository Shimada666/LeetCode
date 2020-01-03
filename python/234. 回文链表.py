# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True
        p=ListNode(-1)
        p.next,s,f=head,p,p
        while f and f.next:
            s,f=s.next,f.next.next
        cur,pre=s.next,None
        s.next=None
        while cur:
            cur.next,pre,cur=pre,cur,cur.next
        a,b=p.next,pre
        while b:
            if b.val!=a.val:
                return False
            a,b=a.next,b.next
        return True