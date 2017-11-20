#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 142_Linked_List_Cycle_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next: return None
        fast, slow, p = head, head, head
        isCycle = False
        #查看是否有环
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                isCycle = True
                break
        if not isCycle: return None
        #寻找环的位置
        while p != slow:
            p, slow = p.next, slow.next
        return p