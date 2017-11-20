#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 561_Array_Partition_I
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
        def arrayPairSum(self, nums):
            return sum(sorted(nums)[::2])