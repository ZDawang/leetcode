#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 303_Range_Sum_Query_Immutable
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def __init__(self, nums):
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)