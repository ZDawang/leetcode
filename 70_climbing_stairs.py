#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-6
#difficulty degree：
#problem: 70_climbing_stairs
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def climbStairs(self, n):
        temp = [1, 2]
        if n < 3:
            return temp[n - 1]
        end_1, end_2 =2, 1
        res = 0
        for i in range(n - 2):
            res = end_2 + end_1
            end_1, end_2 = res, end_1
        return res

solute = Solution()
res = solute.climbStairs(3)
print(res)