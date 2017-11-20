#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 532_K-diff_Pairs_in_an_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #分治，按k的取值分治
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        res = 0
        if k == 0:
            d = {}
            for num in nums:
                if num in d:
                    if d[num] > 1:
                        continue
                    res += 1
                    d[num] = 2
                else:
                    d[num] = 1
            return res
        else:
            d = {}
            for num in nums:
                if num in d:
                    continue
                d[num] = 1
                if num - k in d:
                    res += 1
                if num + k in d:
                    res += 1
            return res