#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-
#difficulty degree：
#problem: 377_Combination_Sum_IV
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路与硬币一样，用dp存储到当前数的最大组合方式
    def combinationSum4(self, nums, target):
        l = len(nums)
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            combinenums = 0
            for j in range(l):
                if i - nums[j] >= 0:
                    combinenums += dp[i - nums[j]]
            dp[i] = combinenums
        return dp[-1]

solute = Solution()
res = solute.combinationSum4([1,2,3], 4)