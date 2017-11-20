#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 697_Degree_of_an_Array.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #记录每个数出现的次数
    #记录每个数的首尾index
    def findShortestSubArray(self, nums):
        #统计
        times, start, end = {}, {}, {}
        for i, num in enumerate(nums):
            if not num in start: start[num] = i
            end[num] = i
            times[num] = times.get(num, 0) + 1
        #选出现最多次的那个的最小范围
        maxtime, res = 0, 0
        for num in times:
            if times[num] > maxtime:
                maxtime = times[num]
                res = end[num] - start[num] + 1
            elif times[num] == maxtime:
                res = min(res, end[num] - start[num] + 1)
        return res
