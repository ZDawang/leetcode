#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-30
#difficulty degree：
#problem: 598_Range_Addition_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m*n
        minx = min([op[0] for op in ops])
        miny = min([op[1] for op in ops])
        return minx * miny
