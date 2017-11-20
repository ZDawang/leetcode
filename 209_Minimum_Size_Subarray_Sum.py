#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 209_Minimum_Size_Subarray_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        sum_temp = 0
        start = 0
        res = len(nums)
        for i in range(len(nums)):
            sum_temp += nums[i]
            if sum_temp >= s:
                while sum_temp - nums[start] >= s:
                    sum_temp -= nums[start]
                    start += 1
                print(start, i, sum_temp)
                res = min(res, i - start + 1)        
        return res if sum_temp >= s else 0

nums = [2,3,1,1,1,1,1]
solute = Solution()
res = solute.minSubArrayLen(5, nums)
print(res)