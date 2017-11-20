#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 206_Reverse_Linked_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next: return head
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre