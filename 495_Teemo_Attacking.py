#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 495_Teemo_Attacking
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(timeSeries[i] - timeSeries[i - 1], duration)
        return res + duration if timeSeries else 0
