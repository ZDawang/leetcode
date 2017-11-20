#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 371_Sum_of_Two_Integers.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        res = a
        while b != 0:
            res = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = res
        return res if res <= MAX else ~(res ^ mask)