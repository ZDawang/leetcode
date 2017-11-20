#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-22
#difficulty degree：
#problem: 223_Rectangle_Area
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #分治，相交，包含，不相交
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (A - C) * (B - D) + (E - G) * (F - H) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)

A, B, C, D, E, F, G, H = -2, -2, 2, 2, -3, -3, 3, -1

solute = Solution()
res = solute.computeArea(A, B, C, D, E, F, G, H)
print(res)