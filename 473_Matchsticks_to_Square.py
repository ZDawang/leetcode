#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #698是把所有的分成k部分。。这题是4部分。。
    def makesquare(self, nums):
        return self.canPartitionKSubsets(nums, 4)

    def canPartitionKSubsets(self, nums, k):
        def dfs(num, mean, visit):
            #若所有数使用完且最后一个组合的结果等于mean，返回True
            if num == 0 and visit == 0: return True
            if visit in dp: return False
            for i in range(len(nums)):
                index = 1 << i
                #当前数没有使用过，且与前面的累加结果的和小于mean，且dfs为True时，返回True
                if (visit & index) and (num + nums[i] <= mean) and dfs((num + nums[i])%mean, mean, visit ^ index):
                    return True
            #将当前组合加入到dp中，避免重复运算。
            dp.add(visit)
            return False

        if not nums or k == 0 or sum(nums)%k != 0: return False
        dp = set()
        return dfs(0, sum(nums)//k, 2**len(nums)-1)