#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 747_Largest_Number_At_Least_Twice_of_Others
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def dominantIndex(self, nums):
        if not nums: return -1
        maxnum = max(nums)
        half = maxnum >> 1
        for num in nums:
            if num == maxnum:
                continue
            if num > half:
                return -1
        return nums.index(maxnum)
