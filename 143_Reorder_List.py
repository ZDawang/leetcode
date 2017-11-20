#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 143_Reorder_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next or not head.next.next: return
        slow, fast = head, head
        #寻找中间点
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next if fast.next else slow
        end = fast.next if fast.next else fast
        #翻转后一半
        pre = None
        start = mid
        while start:
            start.next, start, pre = pre, start.next, start
        #reorder
        start = head
        head = head.next
        while end != mid:
            start.next = end
            start = start.next
            end = end.next

            start.next = head
            start = start.next
            head = head.next

