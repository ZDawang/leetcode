#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 25_Reverse_Nodes_in_k-Group.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #找到每一个k的首尾部，进行翻转
    def reverseKGroup(self, head, k):
        #辅助函数，用于翻转一段序列，返回首尾的节点,以及下一个head的节点
        def reverse(head, k):
            if not head: return head, None, None
            tail = head
            #判断长度
            for i in range(k - 1):
                tail = tail.next
                if not tail: return head, None, None
            pre, cur = head, head.next
            for i in range(k - 1):
                tmp = cur.next
                cur.next = pre
                pre, cur = cur, tmp
            return pre, head, cur

        if not head or k < 2: return head
        tail = ListNode(0)
        pretail = ListNode(0)
        res = pretail
        #当可以继续翻转时
        while tail:
            #获得当前翻转结果的首尾节点，以及下一个翻转的起始节点
            head, tail, nexthead = reverse(head, k)
            #上一个节点的尾部，连到这一个节点的头部
            pretail.next = head
            pretail, head = tail, nexthead
        return res.next







