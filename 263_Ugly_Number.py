#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 263_Ugly_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return num == 1



num = 6
solute = Solution()
res = solute.isUgly(num)
print(res)