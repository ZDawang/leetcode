#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 643_Maximum_Average_Subarray_I.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #滑动窗
    def findMaxAverage(self, nums, k):
        if not nums: return 0
        sums = sum(nums[:k])
        res = sums
        for i in range(len(nums) - k):
            sums = sums - nums[i] + nums[i + k]
            res = max(res, sums)
        return res/float(k)