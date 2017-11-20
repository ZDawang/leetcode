#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 201_Bitwise_AND_of_Numbers_Range.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路，找出范围
    #将数比如35-47，划分成 32 + [3, 15]，再对[3,15]进行分析
    #即找出哪一位1以后会波动
    #当n>=2*k时, 则在m-n里面，有一个2*k-1，有一个2*k，它们相与等于0
    def rangeBitwiseAnd(self, m, n):
        if m == 0: return 0
        k = 1
        while k <= m:
            k = k << 1
        k = k >> 1
        if n >= k << 1: return 0
        return k + self.rangeBitwiseAnd(m - k, n - k)


m, n = 5, 7
