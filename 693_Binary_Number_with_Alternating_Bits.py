#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 693_Binary_Number_with_Alternating_Bits.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def hasAlternatingBits(self, n):
        pre = 0 if (n & 1) else 1
        while n > 0:
            cur = n & 1
            if pre ^ cur == 0:
                return False
            pre, n = cur, n >> 1
        return True