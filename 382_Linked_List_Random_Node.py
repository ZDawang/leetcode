#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 382_Linked_List_Random_Node.py
#time_complecity:  
#space_complecity: 
#beats: 

#蓄水池抽样算法，到第n个节点时，有1/n的概率选择当前结果。
#最后一个选择的节点作为最终结果。
#1*1/2*2/3*3/4... = 1/N
import random
class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        cur, res = head, head.val
        cnt = 1
        while cur:
            randNum = random.randint(1, cnt)
            if randNum == cnt:
                res = cur.val
            cur, cnt = cur.next, cnt + 1
        return res


#直接把node遍历一遍，将结果存到列表中。再直接用随机数取结果。