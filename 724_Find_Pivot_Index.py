#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #双指针不行，因为数组中有负数
    #可以优化为O(1)的空间复杂度
    def pivotIndex(self, nums):
        if not nums: return -1
        n = len(nums)
        sums = [0] * n
        for i in range(n):
            sums[i] += sums[i - 1] + nums[i]
        #选择轴值
        for i in range(n):
            #轴值左边为sums[i] - nums[i]，轴值右边为sums[-1] - sums[i]
            if sums[i] - nums[i] == sums[-1] - sums[i]:
                return i
        return -1

    def pivotIndex2(self, nums):
        if not nums: return -1
        sums, sumtmp = sum(nums), 0
        #选择轴值
        for i in range(len(nums)):
            if sumtmp == sums - sumtmp - nums[i]:
                return i
            sumtmp += nums[i]
        return -1