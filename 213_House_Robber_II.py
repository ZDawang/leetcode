#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-2
#difficulty degree：
#problem: 213_House_Robber_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp数组表示到当前房间抢劫的最大金额
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        def rob2(nums):
            dp = [0, 0]
            for num in nums:
                if num + dp[-2] >= dp[-1]:
                    dp.append(num + dp[-2])
                else:
                    dp.append(dp[-1])
            return dp[-1]
        return max(rob2(nums[: -1]), rob2(nums[1:]))

solute = Solution()
res = solute.rob([2,2,4,3,2,5])
print(res)