#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-2
#difficulty degree：
#problem: 198_House_Robber
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp存储到每个房间的抢劫最大值
    def rob(self, nums):
        dp = [0, 0]
        for num in nums:
            if num + dp[-2] > dp[-1]:
                dp.append(num + dp[-2])
            else:
                dp.append(dp[-1])
        return dp[-1]

