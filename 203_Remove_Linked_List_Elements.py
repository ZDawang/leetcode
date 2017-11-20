#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 203_Remove_Linked_List_Elements.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def removeElements(self, head, val):
        if not head: return None
        #找到第一个非val的元素
        while head.val == val:
            head = head.next
            if not head: return None
        res = head
        while head and head.next:
            tmp = head.next
            #寻找head后第一个非val的node
            while tmp and tmp.val == val:
                tmp = tmp.next
            head.next = tmp
            head = head.next
        return res
