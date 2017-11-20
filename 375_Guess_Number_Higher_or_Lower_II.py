#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 375_Guess_Number_Higher_or_Lower_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi]) for x in range(lo, hi))
        return need[1][n]

solute = Solution()
res = solute.getMoneyAmount(4)
print(res)