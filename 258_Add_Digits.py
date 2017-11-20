#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 258_Add_Digits
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def addDigits(self, num):
        s = sum([int(i) for i in str(num)])
        while s >= 10:
            s = sum([int(i) for i in str(s)])
        return s

num = 38
solute = Solution()
res = solute.addDigits(num)
print(res)