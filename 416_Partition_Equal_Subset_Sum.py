#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-5
#difficulty degree：
#problem: 416_Partition_Equal_Subset_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp存储到目前为止所有的可能加法结果
    def canPartition(self, nums):
        sums = sum(nums)
        if sums%2 == 1: return False
        target = sums//2
        l = len(nums)
        dp = [set() for i in range(l + 1)]
        dp[0] = set([0])
        for i in range(l):
            if not dp[i]: return False
            temp = set([a + nums[i] for a in dp[i] if a + nums[i] <= target])
            dp[i + 1] = dp[i] | temp
            if target in dp[i + 1]:
                return True
        return False

nums = [1, 2, 3, 5]
solute = Solution()
res = solute.canPartition(nums)
print(res)