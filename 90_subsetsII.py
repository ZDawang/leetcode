#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-12
#difficulty degree：
#problem: 90_subsetsII
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = [[]]
        l = 1
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                result += [result[j] + [nums[i]] for j in range(-l, 0)]
            else:
                l = len(result)
                result += [j + [nums[i]] for j in result]
        return result

nums = [0,1,3,4,4]
solute = Solution()
res = solute.subsetsWithDup(nums)
print(res)