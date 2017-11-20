#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 617_Merge_Two_Binary_Trees
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 == None and t2 == None: return None
        if not t1 and t2: return t2
        if t1 and not t2: return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
