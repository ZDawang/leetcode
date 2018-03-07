#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 330_Patching_Array.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #贪心算法。miss用来存储不能凑成的最小数字。
    #可知，若当前的数字比前面可以凑成的数字小，那么可以凑成nums[i]+miss(不包含)内的所有数字。
    #若比miss大，则说明，在[miss, nums[i])范围内的数字无法凑成。此时需要加一个miss，这样，可以凑成到2*miss下的所有数字。
    def minPatches(self, nums, n):
        miss, patch, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patch += 1
        return patch
