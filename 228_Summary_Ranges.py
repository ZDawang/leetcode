#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 228_Summary_Ranges
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路：直接解，找到一段连续的就存进结果里，不连续的就重新计
    def summaryRanges(self, nums):
        if not nums:
            return []
        res, start = [], 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            if i == start + 1:
                res.append(str(nums[i - 1]))
            else:
                res.append(str(nums[start]) + "->" + str(nums[i - 1]))
            start = i
        #最后一个数
        if start + 1 == len(nums):
            res.append(str(nums[-1]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[-1]))
        return res

nums = [0,1,2,4,5,7]
solute = Solution()
res = solute.summaryRanges(nums)
print(res)