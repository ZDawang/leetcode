#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 338_Counting_Bits
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def countBits(self, num):
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i//2] + (i & 1)
        return res

solute = Solution()
res = solute.countBits(5)
