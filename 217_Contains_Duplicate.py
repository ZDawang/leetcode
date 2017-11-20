#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 217_Contains_Duplicate
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        return False