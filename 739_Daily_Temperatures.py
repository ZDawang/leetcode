#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 739_Daily_Temperatures
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #栈
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prei = stack.pop()
                res[prei] = i - prei
            stack.append(i)
        return res