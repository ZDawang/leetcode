#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-11-23
#difficulty degree：
#problem: 312_Burst_Balloons
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp[i][j]表示i到j除了i跟j全部爆炸的最大结果
    #dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    #DP式是将第k个气球作为最后一次爆炸。
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        for length in range(2, l):
            for i in range(l - length):
                j = i + length
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][l - 1]

nums = [3,1,5,8]
solute = Solution()
res = solute.maxCoins(nums)


