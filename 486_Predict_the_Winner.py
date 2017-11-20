#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 486_Predict_the_Winner
#time_complecity:  
#space_complecity: 
#beats: 

#这道题的题意就是，第一个玩家取得的最大收益是否可以大于0
class Solution(object):
    #使用dp来存储i到j的最大收益
    def PredictTheWinner(self, nums):
        if not nums: return True
        l = len(nums)
        if l & 1 == 0: return True
        dp = [[0]*l for i in range(l)]
        for i in range(l - 1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i + 1, l):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][-1] >= 0




    #dp可以重复使用，空间优化为O(n)
    def PredictTheWinner(self, nums):
        if not nums: return True
        l = len(nums)
        if l & 1 == 0: return True
        dp = [0] * l
        for i in range(l - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, l):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0

