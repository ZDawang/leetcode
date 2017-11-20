#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 169_Majority_Element
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def majorityElement(self, nums):
        d = {}
        l = len(nums)
        for num in nums:
            d[num] = d.setdefault(num, 0) + 1
            if d[num] > l//2:
                return num
            