#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 599_Minimum_Index_Sum_of_Two_Lists.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #哈希
    def findRestaurant(self, list1, list2):
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        d = {}
        for i, r in enumerate(list1):
            d[r] = i

        sums = float("inf")
        res = []
        for i, r in enumerate(list2):
            if r in d:
                if d[r] + i < sums:
                    sums = d[r] + i
                    res = [r]
                elif d[r] + i == sums:
                    res.append(r)
        return res
