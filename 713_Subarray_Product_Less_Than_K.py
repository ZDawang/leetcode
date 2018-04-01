#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 713_Subarray_Product_Less_Than_K.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums:
            return 0
        l, prod = 0, 1
        res = 0
        for r in range(len(nums)):
            prod *= nums[r]
            if nums[r] >= k:
                l, prod = r + 1, 1
            else:
                while prod >= k and l < r:
                    l, prod = l + 1, prod//nums[l]
                res += (r-l+1)
        return res