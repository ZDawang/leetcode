#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 190_Reverse_Bits.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def reverseBits(self, n):
        tmp = 2 ** 31
        res = 0
        while n > 0:
            if n & 1:
                res += tmp
            n = n >> 1
            tmp = tmp >> 1
        return res