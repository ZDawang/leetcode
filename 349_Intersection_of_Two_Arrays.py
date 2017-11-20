#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-18
#difficulty degree：
#problem: 349_Intersection_of_Two_Arrays
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)