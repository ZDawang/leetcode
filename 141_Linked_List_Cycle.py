#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 141_Linked_List_Cycle.py
#time_complecity:  
#space_complecity: 
#beats: 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head.next: return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
