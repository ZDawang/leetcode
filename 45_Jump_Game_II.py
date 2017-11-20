#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 45_Jump_Game_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp来存储到当前的最小步数, TLE
    def jump(self, nums):
        l = len(nums)
        dp = [float("inf")] * l
        dp[0] = 0
        for i, maxstep in enumerate(nums):
            for step in range(1, maxstep + 1):
                if i + step < l:
                    dp[i + step] = min(dp[i + step], dp[i] + 1)
        return dp[-1]

    #贪心法 + BFS，记录每一步的最近距离以及最远距离。在这两个距离之间的值则是都可以到达的。
    #不过下一步的范围跟上一步的范围可能会有重叠部分，所以把下一步的最近距离变为上一步的最远距离+1,以免重复计算
    def jump(self, nums):
        l = len(nums)
        if l <= 1: return 0
        level, mindis, maxdis = 0, 0, 0
        while mindis <= maxdis:
            level += 1
            premaxdis = maxdis
            for i in range(mindis, maxdis + 1):
                maxdis = max(i + nums[i], maxdis)
            if maxdis >= l - 1: return level
            mindis = premaxdis
        return level










nums = [2,3,1,1,4]
solute = Solution()
res = solute.jump(nums)
