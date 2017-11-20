#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 448_Find_All_Numbers_Disappeared_in_an_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用442题思路
    def findDisappearedNumbers(self, nums):
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                continue
            else:
                nums[abs(num) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
