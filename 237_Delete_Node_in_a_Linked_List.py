#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 237_Delete_Node_in_a_Linked_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
