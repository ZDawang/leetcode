#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 390_Elimination_Game.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(logn)
    def lastRemaining(self, n):
        l, r, step = 1, n, 1
        ispostive = True
        while l < r:
            #正序时,l为l+step，当消除不到r时，r = r，否则r = r-step
            if ispostive:
                l, r = l + step, r if (r - l) % (step * 2) != 0 else r - step
            else:
                l, r = l if (r - l) % (step * 2) != 0 else l + step, r - step
            step *= 2
            ispostive = not ispostive
        return l

solute = Solution()
res = solute.lastRemaining(8)


        