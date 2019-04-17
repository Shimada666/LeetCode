def deleteDuplicates( head):
    if head == None:
        return head
    cur = head
    while cur.next:  # 下一节点不为空
        if cur.val == cur.next.val:  # 第一次判断，头元素与头元素下一节点的值是否相等。。。
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

