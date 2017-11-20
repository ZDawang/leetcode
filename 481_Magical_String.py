#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 481_Magical_String.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路，双指针
    #一个指针指向计数，一个指针指向结果
    #O(n)
    def magicalString(self, n):
        if n <= 3: return 1 if n >= 1 else 0
        s = [1, 2, 2]
        l, prenum, loc = 0, 2, 2
        while l < n:
            num = 2 if prenum == 1 else 1
            count = s[loc]
            s += [num] * count
            l, prenum, loc = l + count, num, loc + 1
        return s[:n].count(1)

solute = Solution()
res = solute.magicalString(20)