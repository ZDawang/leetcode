#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-27
#difficulty degree：
#problem: 539_Minimum_Time_Difference
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findMinDifference(self, timePoints):
        l = len(timePoints)
        newtime = [0] * l
        for i in range(l):
            tmp = timePoints[i].split(":")
            newtime[i] = int(tmp[0]) * 60 + int(tmp[1])
        newtime.sort()
        res = newtime[0] + 1440 - newtime[-1]
        for i in range(1, l):
            time = newtime[i] - newtime[i - 1]
            res = min(res, time)
        return res
