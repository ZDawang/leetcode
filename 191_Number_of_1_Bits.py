#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 191_Number_of_1_Bits.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #利用与操作来判断是否该位为1
    def hammingWeight(self, n):
        p = 1
        res = 0
        while p <= n:
            if p & n == p: res += 1
            p = p << 1
        return res

    #移位
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            if n & 1:
                res += 1
            n = n >> 1
        return res
