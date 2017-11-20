#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-24
#difficulty degree：
#problem: 365_Water_and_Jug_Problem
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def canMeasureWater(self, x, y, z):
        def gcd(x, y):
            while(y != 0):
                temp = y
                y = x%y
                x = temp
            return x
        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)




solute = Solution()
res = solute.canMeasureWater(4, 6, 8)
print(res)