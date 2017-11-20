#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-30
#difficulty degree：
#problem: 593_Valid_Square
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用向量
    def validSquare(self, p1, p2, p3, p4):
        def d(v1, v2):
            return (v1[0]-v2[0])*(v1[0]-v2[0]) + (v1[1]-v2[1])*(v1[1]-v2[1])
        temp = set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])
        return not 0 in temp and len(temp) == 2

solute = Solution()
res = solute.validSquare([1,0] ,[0,1], [0,-1], [-1,0])
print(res)

