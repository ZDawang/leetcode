#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 442_Find_All_Duplicates_in_an_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思想，若有一个数重复，那么它们作为下标指向的数相同。
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res
        