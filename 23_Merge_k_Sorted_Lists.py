#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10-2
#difficulty degree：
#problem: 23_Merge_k_Sorted_Lists.py
#time_complecity:  
#space_complecity: 
#beats: 
import queue
class Solution(object):
    def mergeKLists(self, lists):
        q = queue.PriorityQueue()
        #获得最初的值
        for node in lists:
            if node != None:
                q.put([node.val, node])
        if q.empty():
            return None
        res = pre = ListNode(0)
        while not q.empty():
            cur = q.get()[1]
            pre.next = cur
            pre = pre.next
            cur = cur.next
            if cur:
                q.put([cur.val, cur])
        return res.next







