#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 138_Copy_List_with_Random_Pointer
#time_complecity:  
#space_complecity: 
#beats: 

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        dic = {}
        m = n = head
        #创建新的节点
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        #绑定对应关系
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

