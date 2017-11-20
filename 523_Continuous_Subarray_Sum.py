#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 523_Continuous_Subarray_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def checkSubarraySum(self, nums, k):
        l = len(nums)
        if k == 0:
            for i in range(1, l):
                if nums[i] == nums[i - 1] and nums[i] == 0:
                    return True
            return False
        remainder = 0
        d = {0: 0}
        for i in range(l):
            remainder = (remainder + nums[i]) % k
            if remainder in d:
                if i - d[remainder] >= 1:
                    return True
            else:
                d[remainder] = i
        return False

nums = [1, 1]
solute = Solution()
res = solute.checkSubarraySum(nums, 2)
print(res)