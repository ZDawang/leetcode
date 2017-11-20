#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-
#difficulty degree：
#problem: 335_Self_Crossing
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #
    def isSelfCrossing(self, x):
        l = len(x)
        if l <= 3: return False
        for i in range(l):
            temp = x[i: i + 6] + [0, 0, 0, 0, 0, 0]
            [a, b, c, d, e, f] = temp[:6]
            if d >= b > 0 and (a >= c or (a >= c - e >= 0 and f >= d - b)):
                return True
        return False


        

nums = [1,1,2,1,1]
solute = Solution()
res = solute.isSelfCrossing(nums)
print(res)