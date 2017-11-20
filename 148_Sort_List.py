#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 148_Sort_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #归并排序,但是空间复杂度为O(logn)
    def sortList(self, head):
        if not head or not head.next: return head
        #找到中间点
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        #将list分成两部分
        pre.next = None
        return self.merge(self.sortlist(head), self.sortList(slow))

    #将两个listNode合并成一个listNode
    def merge(self, h1, h2):
        head = tail = ListNode(0)
        while h1 and h2:
            if h1.val <= h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next
        tail.next = h1 or h2
        return head.next

