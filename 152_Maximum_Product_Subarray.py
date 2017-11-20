#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 152_Maximum_Product_Subarray
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def maxProduct(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        res = nums[0]
        min_local = nums[0]
        max_local = nums[0]
        for i in range(1, l):
            min_local, max_local = min([nums[i], nums[i]*min_local, nums[i]*max_local]), max([nums[i], nums[i]*min_local, nums[i]*max_local])
            res = max(res, max_local)
        return res
    



nums = [2,-5,-2,-4,3]
solute = Solution()
res = solute.maxProduct(nums)
print(res)