#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 575_Distribute_Candies
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def distributeCandies(self, candies):
        d = collections.defaultdict(int)
        for candie in candies:
            d[candie] += 1
        return min(len(d.keys()), len(candies)//2)