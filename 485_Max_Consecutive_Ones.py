#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 485_Max_Consecutive_Ones
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        cnt = 0
        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
            res = max(res, cnt)
        return res