#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 746_Min_Cost_Climbing_Stairs.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP，dp[i]存储到当前的最小费用。
    def minCostClimbingStairs(self, cost):
        if len(cost) <= 2:
            return min(cost or [0])
        dp = [0 for i in range(len(cost) + 1)]
        #计算到i处的所需最小费用。len(cost)处即为终点
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]

    #空间复杂度优化.
    def minCostClimbingStairs2(self, cost):
        if len(cost) <= 2:
            return min(cost or [0])
        step2, step1 = 0, 0
        for i in range(2, len(cost) + 1):
            step1, step2 = min(step2 + cost[i - 2], step1 + cost[i - 1]), step1
        return step1