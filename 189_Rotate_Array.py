#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 189_Rotate_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

nums = [1,2,3,4,5,6]
solute = Solution()
solute.rotate(nums, 2)
print(nums)