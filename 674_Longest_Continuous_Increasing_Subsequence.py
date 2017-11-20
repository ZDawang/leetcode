#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 674_Longest_Continuous_Increasing_Subsequence.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        res, tmp = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
        return max(res, tmp)

    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        res, tmp = 1, 1
        for i in range(1, len(nums)):
            tmp = tmp + 1 if nums[i] > nums[i - 1] else 1
            res = max(res, tmp)
        return res