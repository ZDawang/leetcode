#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 525_Contiguous_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findMaxLength(self, nums):
        d = {0: -1}
        sumtemp = 0
        res = 0
        for i in range(len(nums)):
            sumtemp = sumtemp + 1 if nums[i] else sumtemp - 1
            if sumtemp in d:
                res = max(res, i - d[sumtemp])
            else:
                d[sumtemp] = i
        return res

nums = [0, 1]
solute = Solution()
res = solute.findMaxLength(nums)
print(res)