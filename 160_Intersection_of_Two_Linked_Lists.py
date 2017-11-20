#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 160_Intersection_of_Two_Linked_Lists.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #最直观的思路：
    #先统计A与B的长度，把A与B放在离尾部相同距离的地方，一起向前走
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        #先统计长度
        la, lb = 1, 1
        hA, hB = headA, headB
        while hA.next:
            hA, la = hA.next, la + 1
        while hB.next:
            hB, lb = hB.next, lb + 1
        
        #调整A或者B，使他们离尾部的距离相同
        headA, headB = (headA, headB) if la > lb else (headB, headA)
        remove = abs(la - lb)
        for i in range(remove):
            headA = headA.next

        #向前遍历，直到找到相同的节点
        while headA:
            if headA == headB: return headA
            headA, headB = headA.next, headB.next
        return None




