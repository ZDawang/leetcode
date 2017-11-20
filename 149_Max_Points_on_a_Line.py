#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 149_Max_Points_on_a_Line.py
#time_complecity:  
#space_complecity: 
#beats: 
import numpy as np
class Solution(object):
    #对于每个点都找到经过它的并经过点数最多的直线
    #与y轴平行的点，用float("inf")表示斜率。
    #与point重合的点，用一个same_point表示
    def maxPoints(self, points):
        l, res = len(points), 0
        for i in range(l):
            samePoint, d = 0, {}
            for j in range(i + 1, l):
                dx, dy = points[j].x - points[i].x, points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    samePoint += 1
                elif dx == 0:
                    d[float("inf")] = d.get(float("inf"), 0) + 1
                else:
                    slope = dy * np.longdouble(1) / dx
                    d[slope] = d.get(slope, 0) + 1
            maxnum = max(d[key] for key in d) + samePoint if d else samePoint
            #还有这个点本身，所以maxnum+1
            res = max(res, maxnum + 1)
        return res

points = [[0,0],[94911151,94911150],[94911152,94911151]]
solute = Solution()
res = solute.maxPoints(points)